from PIL import Image

# باز کردن عکس
img = Image.open('profile-square-11.png')

# کاهش سایز به ۶۰۰px
img.thumbnail((600, 600), Image.LANCZOS)

# ذخیره به WebP با کیفیت ۸۰٪
img.save('profile-square.webp', 'WEBP', quality=80, optimize=True)

# چک کردن سایز
import os
size_kb = os.path.getsize('profile-square.webp') / 1024
print(f"حجم عکس جدید: {size_kb:.1f} KB")