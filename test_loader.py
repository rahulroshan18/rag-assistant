from loaders.pdf_loader import load_pdf

text = load_pdf("data/Rahul_Roshan_Resume.pdf")

print("=" * 60)
print("PDF Loaded Successfully")
print("=" * 60)

print(f"Total Characters : {len(text)}")
print()

print("First 300 Characters:")
print("-" * 60)

print(text[:300])