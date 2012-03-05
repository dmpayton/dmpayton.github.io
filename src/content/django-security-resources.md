Title: Django Security Resources
Date: 2012-01-09
Intro: A collection of literature, apps, and presentations to help you secure your Django site.
Tags: django, security

Security is a complex beast and is not just limited to the application level (i.e., your Django project); there are several layers above and below your web app where a security hole could be disastrous for you or your users. Only a full security audit from a competent security professional can tell you if your site is secure.

That said, I hope this post will help ensure your Django site is *reasonably* secure. I am by no means an expert in web application security, and this post is as much for my own reference as it is for yours. I will try to keep this information up to date as time goes on. If you have any suggestions, [please let me know](/).

<!-- **Last Updated: 2012-01-09** -->

## Literature

[Django Documentation &mdash; Security in Django](https://docs.djangoproject.com/en/dev/topics/security/)

[The Django Book &mdash; Chapter 20: Security](http://www.djangobook.com/en/2.0/chapter20/)

## Django Apps

[django-admin-honeypot](https://github.com/dmpayton/django-admin-honeypot) &mdash; "A fake Django admin login screen to notify admins of attempted unauthorized access." <span class="small light">(Disclaimer: I made this.)</span>

[django-axes](https://github.com/codekoala/django-axes) &mdash; "A very simple way for you to keep track of failed login attempts, both for the Django admin and for the rest of your site." Useful for throttling login attempts and preventing brute-force password attacks.

[django-bcrypt](https://bitbucket.org/dwaiter/django-bcrypt) &mdash; "Makes it easy to use bcrypt to hash passwords with Django. [You should be using bcrypt.](http://codahale.com/how-to-safely-store-a-password/)"

[django-secure](https://github.com/carljm/django-secure) &mdash; "Helping you remember to do the stupid little things to improve your Django site's security."

[django-xframeoptions](https://github.com/paulosman/django-xframeoptions) &mdash; Django middleware to add the `X-Frame-Options` HTTP header to prevent clickjacking attacks.

## Presentations

[Advanced Security Topics, DjangoCon 2011](http://blip.tv/djangocon/advanced-security-topics-5573326) [video] &mdash; "An in-depth look (with demonstrations) at the how and why of several advanced security topics. Discussion of ways to improve security of the framework moving forward."

[Django Web Application Security
](http://www.slideshare.net/levigross/django-web-application-security) [slides]
