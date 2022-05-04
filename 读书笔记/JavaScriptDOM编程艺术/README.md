## JavaScript语法
- 用JavaScript编写的代码必须通过HTML/XHTML文档才能执行
<br>
方式一：<br>
将JavaScript代码放到文档`<head>`标签中的`<script>`标签之间<br>
方式二：<br>
把js代码作为一个.js的独立文件，在文档的`<head>`部分放一个`<script>`标签，并把它的src属性指向该文件<br>
方式三：<br>
把`<script>`标签放到HTML文档的最后，`</body>` 标签之前
<br>

```
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8"/>
  <title>Example</title>
</head>
<body>
  <script src="file.js"></script>
</body>
```
<br>

* 程序语言分为解释型和编译型两大类，Java或c++等语言需要一个编译器，编译器是一种程序，把高级程序语言编写出的源代码翻译为直接在计算器上执行的文件。<br>
* 解释型程序设计语言不需要编译器，它们仅需要解释器，对js语言，web浏览器负责完成有关的解释和执行工作。浏览器中如果没有解释器，js代码就无法执行