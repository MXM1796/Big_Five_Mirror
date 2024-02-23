Weblink: https://developer.chrome.com/docs/extensions/mv3/getstarted/extensions-101/
# Chrome Extensions 101 - Chrome for Developers
Explore basic concepts of Chrome extension development.

Published on Tuesday, October 4, 2022 • Updated on Friday, September 8, 2023

This page describes what an extension is and provides a brief introduction to Chrome extension development. It also includes links to [beginner tutorials](#building).

What are extensions?
--------------------

Chrome extensions enhance the browsing experience by adding features and functionality to the Chrome browser, providing things like:

*   Productivity tools.
*   Web page content enrichment.
*   Information aggregation.

These are just a few examples of the many things that extensions can do. Visit the [Chrome Web Store](https://chrome.google.com/webstore/) to see thousands of examples of published extensions.

Web technologies
----------------

Extensions are written with the same web technologies used to create web applications:

*   [HTML](https://web.dev/learn/html/) is used as a content markup language.
*   [CSS](https://web.dev/learn/css/) is used for styling.
*   [JavaScript](https://developer.mozilla.org/docs/Learn/JavaScript) is used for scripting and logic.
*   [Web platform APIs](https://developer.mozilla.org/docs/Web/API) let you use virtually any feature available to a standard web page.

Before moving forward, we recommend that you become familiar with these technologies.

Chrome extension APIs
---------------------

Extensions can use all the [JavaScript APIs](https://developer.mozilla.org/docs/Web/API) that the browser provides. What makes extensions more powerful than a web app is their access to [Chrome APIs](https://developer.chrome.com/docs/extensions/reference/). The following are just a few examples of what extensions can do:

*   Change the functionality or behavior of a website.
*   Allow users to collect and organize information across websites.
*   Add features to Chrome DevTools.

See [Extension development overview](https://developer.chrome.com/docs/extensions/mv3/devguide/) for a complete list of API capabilities.

Extension files
---------------

Extensions contain different files, depending on the functionality provided. The following are some of the most frequently used files:

The manifest

The extension's [manifest](https://developer.chrome.com/docs/extensions/mv3/manifest/) is the only required file that **must** have a specific file name: `manifest.json` . It also has to be located in the extension's root directory. The manifest records important metadata, defines resources, declares permissions, and identifies which files to run in the background and on the page.

The service worker

The extension [service worker](https://developer.chrome.com/docs/extensions/mv3/service_workers/) handles and listens for browser events. There are many types of events, such as navigating to a new page, removing a bookmark, or closing a tab. It can use all the [Chrome APIs](https://developer.chrome.com/docs/extensions/reference/), but it cannot interact directly with the content of web pages; that’s the job of content scripts.

Content scripts

[Content scripts](https://developer.chrome.com/docs/extensions/mv3/content_scripts/) execute Javascript in the context of a web page. They can also read and modify the [DOM](https://developer.mozilla.org/docs/Web/API/Document_Object_Model) of the pages they're injected into. Content Scripts can only use a subset of the [Chrome APIs](https://developer.chrome.com/docs/extensions/reference/) but can indirectly access the rest by exchanging messages with the extension service worker.

The popup and other pages

An extension can include various HTML files, such as a [popup](https://developer.chrome.com/docs/extensions/mv3/user_interface/#popup), an [options page](https://developer.chrome.com/docs/extensions/mv3/options/), and [other HTML pages](https://developer.chrome.com/docs/extensions/mv3/architecture-overview/#html-files). All these pages have access to [Chrome APIs](https://developer.chrome.com/docs/extensions/reference/).

Visit [Extensions Architecture](https://developer.chrome.com/docs/extensions/mv3/architecture-overview/) and [Designing the user interface](https://developer.chrome.com/docs/extensions/mv3/user_interface/) to dive deeper.

Many extensions use a popup to customize the user experience, however this is _not_ required. For example, the [reading time](https://developer.chrome.com/docs/extensions/mv3/getstarted/tut-reading-time/) and [focus mode](https://developer.chrome.com/docs/extensions/mv3/getstarted/tut-focus-mode/) extension tutorials do not include a popup.

Developing your extension
-------------------------

Even though web applications and extensions share many of the same technologies, the extension development experience is different. Check out [Development Basics](https://developer.chrome.com/docs/extensions/mv3/getstarted/development-basics/) to create a "Hello, Extensions" example and familiarize yourself with the extension development workflow.

Debugging your extension
------------------------

Extensions can access the same Chrome DevTools as web pages. To become an expert in debugging extensions, you will need to know how to locate logs and errors of the different extension components. Check out [Debugging extensions](https://developer.chrome.com/docs/extensions/mv3/tut_debugging/) to learn techniques for debugging your extension.

Designing your extension features
---------------------------------

When you start designing your extension and choosing which features to support, make sure it fulfills a [single purpose](https://developer.chrome.com/docs/extensions/mv3/single_purpose/) that is narrowly defined and easy to understand. This will allow your extension to be distributed through the Chrome Web Store.

"Single purpose" can refer to one of two aspects of an extension:

1.  An extension can have a single purpose limited to a narrow _focus area_ or _subject matter_. For example, "news headlines", "weather", "comparison shopping".
    
2.  Or, an extension can have a single purpose limited to a narrow _browser function_. For example, "new tab page", "tab management", or "search provider".
    

Regardless of the extension's purpose, the experience provided by the extension must respect the user's other settings and preferences.

See [Extension quality guidelines](https://developer.chrome.com/docs/extensions/mv3/single_purpose/) for additional details.

Distributing your extension
---------------------------

You can set up a developer account with the [Chrome Web Store](https://chrome.google.com/webstore/) to host and distribute your extension. Bear in mind that extensions must adhere to the [developer program policies](https://developer.chrome.com/docs/webstore/program-policies/).

See [Publish in the Chrome Web Store](https://developer.chrome.com/docs/webstore/publish/) to learn how to distribute your extension.

Some organizations use enterprise policies to install extensions on their user's devices. These extensions may either be fetched from the Chrome Web Store or hosted on the organization's web servers. Read about both in [Enterprise publishing options](https://developer.chrome.com/docs/webstore/cws-enterprise/).

🚀 Ready to start building?
---------------------------

Choose any of the following tutorials to begin your extension learning journey.


|Extension   |What you will learn                                                    |
|------------|-----------------------------------------------------------------------|
|Reading time|To insert an element on every page automatically.                      |
|Focus Mode  |To run code on the current page after clicking on the extension action.|
|Tabs Manager|To create a popup that manages browser tabs.                           |


As a bonus, these tutorials were designed to improve your experience when reading the Chrome extension and Chrome Web store documentation:

*   Reading time adds the expected reading time to each documentation articles.
*   Focus mode changes the style of the page to help you concentrate on the documentation content.
*   Tabs manager allows you to organize your extension documentation tabs.

Updated on Friday, September 8, 2023 • [Improve article](https://github.com/GoogleChrome/developer.chrome.com/blob/main/site/en/docs/extensions/mv3/getstarted/extensions-101/index.md)