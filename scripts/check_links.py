# -*- coding: utf-8 -*-
"""批量链接核查器（供《资源大全》使用，5 轮迭代产物的验证工具）。
用法: python check_links.py <urls.json> <out.json> [start] [end]  （省略范围=全量）
策略: HEAD 直连 -> GET 直连 -> 代理(127.0.0.1:7897) HEAD/GET。
分类: ok(2xx/3xx) guard(403/405/429 浏览器可达) auth(401/451) fail(其他/异常)
"""
import json, os, sys, ssl, socket
import urllib.request, urllib.error
from concurrent.futures import ThreadPoolExecutor, as_completed

UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/126.0 Safari/537.36")
PROXY = os.environ.get("CHECK_PROXY", "http://127.0.0.1:7897")
CTX = ssl.create_default_context()
CTX.check_hostname = False
CTX.verify_mode = ssl.CERT_NONE


def _req(url, method, proxy=None, timeout=10, redirect=True):
    handlers = [urllib.request.HTTPSHandler(context=CTX)]
    if proxy:
        handlers.append(urllib.request.ProxyHandler({"http": proxy, "https": proxy}))
    else:
        handlers.append(urllib.request.ProxyHandler({}))  # 强制直连
    if not redirect:
        class NoRedirect(urllib.request.HTTPRedirectHandler):
            def redirect_request(self, *a, **k):
                return None
        handlers.append(NoRedirect())
    op = urllib.request.build_opener(*handlers)
    req = urllib.request.Request(url, method=method, headers={
        "User-Agent": UA, "Accept": "*/*", "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
        "Range": "bytes=0-4096"})
    try:
        r = op.open(req, timeout=timeout)
        code = r.status
        r.read(1024); r.close()
        return code, None
    except urllib.error.HTTPError as e:
        try:
            e.read(512); e.close()
        except Exception:
            pass
        return e.code, None
    except Exception as e:
        return None, f"{type(e).__name__}: {str(e)[:120]}"


def classify(code):
    if code is None:
        return None
    if 200 <= code < 400:
        return "ok"
    if code in (403, 405, 429):
        return "guard"
    if code in (401, 451):
        return "auth"
    return "fail"


def check(url):
    # 1) 直连 HEAD
    code, err = _req(url, "HEAD")
    cls = classify(code)
    if cls == "ok":
        return {"url": url, "cls": "ok", "status": code, "via": "direct-head", "note": ""}
    # 2) 直连 GET（HEAD 常被 403/405 拦截）
    if cls in (None, "guard") or cls == "fail":
        code2, err2 = _req(url, "GET")
        cls2 = classify(code2)
        if cls2 == "ok":
            return {"url": url, "cls": "ok", "status": code2, "via": "direct-get", "note": ""}
        if cls2 == "guard":
            return {"url": url, "cls": "guard", "status": code2, "via": "direct-get", "note": ""}
        if cls2 == "auth":
            return {"url": url, "cls": "auth", "status": code2, "via": "direct-get", "note": ""}
        code, err = code2, err2
    # 3) 代理重试
    for method in ("HEAD", "GET"):
        code_p, err_p = _req(url, method, proxy=PROXY, timeout=15)
        cls_p = classify(code_p)
        if cls_p in ("ok", "guard", "auth"):
            return {"url": url, "cls": cls_p, "status": code_p, "via": "proxy-" + method, "note": ""}
    return {"url": url, "cls": "fail", "status": None,
            "via": "none", "note": (err or "") + (f" | proxy: {err_p}" if err_p else "")}


def main():
    if len(sys.argv) == 3:
        urls_file, out_file, start, end = sys.argv[1], sys.argv[2], 0, None
    else:
        urls_file, start, end, out_file = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), sys.argv[4]
    urls = json.load(open(urls_file, encoding="utf-8"))
    batch = urls[start:end] if end is not None else urls[start:]
    results = []
    with ThreadPoolExecutor(max_workers=24) as pool:
        futs = {pool.submit(check, u): u for u in batch}
        for f in as_completed(futs):
            results.append(f.result())
    results.sort(key=lambda x: (x["cls"], x["url"]))
    json.dump(results, open(out_file, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    from collections import Counter
    cnt = Counter(r["cls"] for r in results)
    print(f"batch {start}-{end}: {dict(cnt)}")
    for r in results:
        if r["cls"] in ("fail",):
            print("FAIL ", r["status"], r["url"], "|", r["note"][:150])


if __name__ == "__main__":
    main()
