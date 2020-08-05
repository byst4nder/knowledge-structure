<p align="center"><img src="https://cloud.githubusercontent.com/assets/1745854/14191006/397082b2-f75b-11e5-9f5b-6016d069556b.png"/>
</p>

# epub-press-clients
> Easy to use clients for building ebooks with [EpubPress](https://epub.press).

Backend code can be found in [haroldtreen/epub-press](https://github.com/haroldtreen/epub-press).

Follow us on [Twitter](https://twitter.com/Epub_Press).

## Overview
EpubPress is a service for stitching articles/blogs/webpages into a customized ebook.

chrome下通过原包直接安装。避免翻墙下载。
1、直接将压缩包解压出来，
2、然后在chrome中设置中，选择 拓展程序 启动开发者模式
3、加载已解压的拓展程序，选择此目录。
4、D:\epub-press-clients-master\packages\epub-press-chrome\app
5、完成安装，然后选择一个网页测试
6、设置kindle邮箱和epub标题title。

#### 🌟 Benefits 🌟
EpubPress makes reading the web more enjoyable!

- Downloads your articles for offline reading.
- Books are compatible with all your iPhone, Android, Kindle, Nook, etc.
- Removes website boilerplate and ads. Just. Clean. Content.
- Lets you group information together (eg. "News from this week", "Top 10 travel articles").
- Easy to sharing with friends.

## Packages 📦

### epub-press-chrome

[![Chrome Web Store](https://img.shields.io/chrome-web-store/v/pnhdnpnnffpijjbnhnipkehhibchdeok.svg?maxAge=2592000)](https://chrome.google.com/webstore/detail/epubpress-read-the-web-of/pnhdnpnnffpijjbnhnipkehhibchdeok)
[![Chrome Web Store](https://img.shields.io/chrome-web-store/d/pnhdnpnnffpijjbnhnipkehhibchdeok.svg?maxAge=2592000)](https://chrome.google.com/webstore/detail/epubpress-read-the-web-of/pnhdnpnnffpijjbnhnipkehhibchdeok)

Source code for the EpubPress chrome extension. The extension allows you to build ebooks by selecting articles from your currently open tabs.

**It is available on the [Chrome Store](https://chrome.google.com/webstore/detail/epubpress/pnhdnpnnffpijjbnhnipkehhibchdeok)**  

See the Readme [here](./packages/epub-press-chrome/README.md)

### epub-press-js

[![npm](https://img.shields.io/npm/v/epub-press-js.svg?maxAge=2592000)](https://www.npmjs.com/package/epub-press-js)
[![npm](https://img.shields.io/npm/dt/epub-press-js.svg?maxAge=2592000)](https://www.npmjs.com/package/epub-press-js)

A javascript library for creating books with EpubPress.

**It is available on [npm](https://www.npmjs.com/package/epub-press-js)**

See the Readme [here](./packages/epub-press-js/README.md)

### epub-press-widgets

A set of ready to use widgets for integration by publishers. Give your users the ability to download your content in an ebook.

**Development/release is on the Roadmap.***

See the Readme [here](./packages/epub-press-widgets/README.md)


## Roadmap 🛣
- Widgets.
- Ability to share your generated creations with others.
- Custom cover page.
- Extra metadata (eg. author).
- Detection for pages with a list of links (eg. OneTab, Feedly, RSS Feeds) and show those links.

Have any awesome ideas? Suggestions? Feature requests? Would love to hear them!  
feedback@epub.press

## Bug Reporting 🐛
Create an [issue](https://github.com/haroldtreen/epub-press-clients/issues) in Github.

**OR**

Send a help request to [support@epub.press](mailto:support@epub.press).  
Please include as much information as possible (eg. version, os, reproduction steps, screenshots)

## Acknowledgements 👏

- Icon created by Picol.org (http://www.picol.org/)
- Content extraction using `node-readability` (https://www.npmjs.com/package/node-readability)
- epub construction using `nodepub` (https://www.npmjs.com/package/nodepub)
