import pandas as pd
import qrcode
import os

# Load student data
df = pd.read_csv("certificates.csv", dtype=str)

# Ensure qr_codes folder exists
output_dir = os.path.join(os.getcwd(), "qr_codes")
os.makedirs(output_dir, exist_ok=True)

# Unique batch IDs
batches = df['batch_id'].dropna().unique()

for batch in batches:
    url = f"https://4dtsregistrar.github.io/CAA-II-Refresher-Training-Batch-2-CY-2025/verify.html?id={batch}"

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")

    file_path = os.path.join(output_dir, f"{batch}.png")
    img.save(file_path)

    print(f"QR for {batch} generated: {url}")
    print(f"  -> Saved at {file_path}")
