from pypdf import PdfReader

for path in [
    r"C:\Users\BS01329\Downloads\Ali Haider Talukder Akib - Resume.pdf",
    r"C:\Users\BS01329\Downloads\Ali Haider Talukder Akib_CV.pdf",
]:
    print("=" * 60)
    print(path)
    r = PdfReader(path)
    for pi, page in enumerate(r.pages):
        annots = page.get("/Annots")
        if not annots:
            continue
        for a in annots:
            obj = a.get_object()
            act = obj.get("/A")
            if act and act.get("/URI"):
                print(f"  page {pi}: {act.get('/URI')}")
