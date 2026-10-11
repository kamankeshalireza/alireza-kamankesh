from django.db import migrations

POST_1 = dict(
    slug="alireza-kamankesh-web-developer",
    title_en="Alireza Kamankesh — Django & Python Web Developer",
    title_fa="علیرضا کمانکش — توسعه‌دهنده وب با پایتون و جنگو",
    excerpt_en="Who I am, what I build with Django and Python, and where to find my projects.",
    excerpt_fa="علیرضا کمانکش هستم؛ دانشجوی مهندسی کامپیوتر و توسعه‌دهنده وب. اینجا می‌خوانید چه چیزهایی با پایتون و جنگو می‌سازم و پروژه‌هایم را کجا ببینید.",
    content_en="""Hi, I'm **Alireza Kamankesh**, a Computer Engineering student and web developer working mainly with **Python and Django**.

## What I build

- E-commerce websites with admin panels
- Persian (RTL) business websites with a strong SEO foundation
- Cafe menu management systems
- Telegram bots and web scrapers in Python

## Where to see my work

My projects are listed on the [portfolio page](/portfolio/), and the source code of many of them is on [GitHub](https://github.com/kamankeshalireza).

If you have a project in mind, you can reach me from the [contact page](/contact/).
""",
    content_fa="""سلام، من **علیرضا کمانکش** هستم؛ دانشجوی مهندسی کامپیوتر و توسعه‌دهنده وب که بیشتر با **پایتون و جنگو** کار می‌کنم.

## چه چیزهایی می‌سازم

- فروشگاه اینترنتی همراه با پنل مدیریت
- وب‌سایت‌های فارسی (راست‌به‌چپ) کسب‌وکارها با پایه‌ی سئوی قوی
- سیستم مدیریت منوی کافه
- ربات تلگرام و وب اسکرپر با پایتون

## نمونه‌کارها را کجا ببینید

پروژه‌هایم در [صفحه نمونه‌کارها](/fa/portfolio/) فهرست شده‌اند و کد منبع بسیاری از آن‌ها در [گیت‌هاب](https://github.com/kamankeshalireza) در دسترس است.

اگر پروژه‌ای در ذهن دارید، از [صفحه تماس](/fa/contact/) با من در ارتباط باشید.
""",
)

POST_2 = dict(
    slug="from-mobile-repair-to-web-development",
    title_en="From Mobile Phone Repair to Web Development: My Story",
    title_fa="از تعمیرات موبایل تا توسعه وب؛ مسیر علیرضا کمانکش",
    excerpt_en="How a hardware repair background shaped the way I debug, build and deploy web projects.",
    excerpt_fa="چطور سابقه‌ی تعمیرات سخت‌افزار موبایل روی نگاه من به عیب‌یابی، ساخت و استقرار پروژه‌های وب اثر گذاشت.",
    content_en="""I started with hardware: diagnosing broken phones, replacing components and restoring devices. That work taught me patience and a structured way to find the real cause of a problem.

## Moving to software

While studying Computer Engineering I moved into web development with **Python and Django**. The debugging mindset from repair work transfers directly: reproduce the issue, isolate it, fix the root cause, then verify.

## What I do today

I build and deploy full-stack projects — e-commerce sites, management panels and automation tools — and I still offer certified mobile repair.

You can see the results on my [portfolio](/portfolio/).
""",
    content_fa="""کارم را با سخت‌افزار شروع کردم: عیب‌یابی گوشی‌های خراب، تعویض قطعات و بازیابی دستگاه‌ها. این کار به من صبر و روشی ساختارمند برای پیدا کردن علت واقعی مشکل یاد داد.

## ورود به دنیای نرم‌افزار

همزمان با تحصیل در مهندسی کامپیوتر، با **پایتون و جنگو** وارد توسعه وب شدم. نگاه عیب‌یابی از دنیای تعمیرات مستقیم به برنامه‌نویسی منتقل می‌شود: مشکل را بازتولید کن، جدا کن، ریشه را رفع کن و بعد صحت را بسنج.

## امروز چه می‌کنم

پروژه‌های فول‌استک می‌سازم و مستقر می‌کنم — فروشگاه اینترنتی، پنل مدیریت و ابزارهای اتوماسیون — و همچنان خدمات تعمیرات دارای گواهی موبایل ارائه می‌دهم.

نتیجه‌ی کارها را در [نمونه‌کارها](/fa/portfolio/) ببینید.
""",
)


def create_posts(apps, schema_editor):
    Post = apps.get_model("blog", "Post")
    for d in (POST_1, POST_2):
        Post.objects.update_or_create(
            slug=d["slug"],
            defaults=dict(
                title=d["title_en"], title_en=d["title_en"], title_fa=d["title_fa"],
                excerpt=d["excerpt_en"], excerpt_en=d["excerpt_en"], excerpt_fa=d["excerpt_fa"],
                content=d["content_en"], content_en=d["content_en"], content_fa=d["content_fa"],
                is_published=True,
            ),
        )


def remove_posts(apps, schema_editor):
    apps.get_model("blog", "Post").objects.filter(
        slug__in=[POST_1["slug"], POST_2["slug"]]).delete()


class Migration(migrations.Migration):
    dependencies = [("blog", "0002_post")]
    operations = [migrations.RunPython(create_posts, remove_posts)]
