Automating Web Accessibility
============================

:date: 2012-03-17
:intro: Bring web accessibility testing to your website
:tags: python, accessibility

`PyCon`_ was last week, and two things really caught my eye. First, `Robbie Clemons`_ gave a talk on `How to make your websites more accessible`_. Second, `Katie Cunningham`_ had a poster on `Accessibility and You`_. I found both of these very informative, and I was glad to see people talking about making the web accessible.

Let's talk about web accessibility
----------------------------------

**Web accessibility is important**. In the United States there are tens of millions of people with a wide range of disabilities. Many websites simply lose these people as users and as customers because they are not accessible.

**Web accessibility is easy**. If you do it right, web accessibility is really not all that complicated. In fact, there's a lot of overlap between web accessibility and SEO. The problem is that SEO tuning is where a lot of developers tend to stop.

During PyCon, a co-worker and I got to talking about how to make the web more accessible. What if accessibility testing was easier? What if we could automate it? What if our test suite failed if our site wasn't accessible? Hmm...

Introducing webalin
-------------------

`Webalin`_ is an accessibility linter that can be used from the command line or within your code. It can take a full HTML document or a URL, and runs accessibility tests over the markup and spits out potential issues.

A Short Demo
~~~~~~~~~~~~

`Section 508`_ of the `Rehabilitation Act of 1973`_ mandates that U.S. Federal agencies must make their electronic and information technology accessible to people with disabilities.

Recently the U.S. government has started asserting its control over several top-level domains, and has seized many domains over (potentially questionable?) copyright infringement allegations. If you head over to `MegaUpload`_, you can see that the domain seizure notice consists of a single image with *lots* of text. Lets see how accessible this is:

.. code-block:: bash

    $ webalin http://megaupload.com
    E: -: <!DOCTYPE> is missing
    E: 4: <img:/banner.jpg> is missing [alt]

The command-line utility output messages as ``[type]: [line no]: [message]``.

As you can see, this is clearly **not** Section 508 compliant. A visually disabled person with a screen reader would have absolutely no idea what is going on with the domain. (Someone should really get on that...)

Looking to the future
~~~~~~~~~~~~~~~~~~~~~

The current incarnation of webalin only checks the markup. This is a good start, but there's so much more to testing accessibility. How accessible is your page after the CSS and JS have been loaded?

In the future, I would like to explore using an in-browser testing framework -- such as `Selenium`_ -- to create a more comprehensive test suite. Django 1.4 will have better integration for this kind of thing and will likely be a good place to start.

Get involved! Please?
~~~~~~~~~~~~~~~~~~~~~

I am by no means an accessibility expert. At best, I am a mediocre programmer with an interest in helping make the web accessible. :) Please do not hesitate contribute in any way, *especially* if you have experience in this area.

* `Fork webalin on Github`_
* `Documentation on ReadTheDocs`_

.. _PyCon: https://us.pycon.org/2012/
.. _Robbie Clemons: http://rclemons.net/
.. _Katie Cunningham: http://therealkatie.net/
.. _How to make your websites more accessible: http://pyvideo.org/video/633/how-to-make-your-websites-more-accessible
.. _Accessibility and You: http://pyvideo.org/video/706/12-accessibility-and-you
.. _Webalin: https://github.com/dmpayton/webalin
.. _Section 508: http://section508.gov/
.. _Rehabilitation Act of 1973: http://en.wikipedia.org/wiki/Rehabilitation_Act_of_1973#Section_508
.. _MegaUpload: http://megaupload.com/
.. _Selenium: http://seleniumhq.org/
.. _Fork webalin on Github: https://github.com/dmpayton/webalin
.. _Documentation on ReadTheDocs: http://webalin.readthedocs.org/
