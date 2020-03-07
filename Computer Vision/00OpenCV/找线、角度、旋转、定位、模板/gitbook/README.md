# 图像矫正问题

> 对于**图像矫正**问题，在图像处理领域很多：人民币的矫正、文本的矫正、车牌的矫正、身份证的矫正等等。识别这些图像，必须优先将图像还原好，不然后期的数字分割、数字识别和文字识别难度加大。
>

**发票**

![invoice.jpg](https://wx3.sinaimg.cn/mw690/005Q1p9vgy1gc9hfz34spj30pe0f775z.jpg)

**文本**

![text.jpg](https://wx4.sinaimg.cn/mw690/005Q1p9vgy1gc9jh4wfy5j30po0edgtd.jpg)

**文本**

![text2](https://wx3.sinaimg.cn/mw690/005Q1p9vgy1gc9k8l85p4j30l70pt4iq.jpg)

> 目标：**图像旋转** + **图像提取**



参考文献1：[OpenCV探索之路（十六）：图像矫正技术深入探讨](https://www.cnblogs.com/skyfsm/p/6902524.html)

参考文献2：[Python-OpenCV：文本图像小角度旋转矫正（边缘投影法）](https://www.jianshu.com/p/e94242f6bee9)

<script type="text/javascript">  /* 鼠标特效 */  var a_idx = 0;  jQuery(document).ready(function($) {      $("body").click(function(e) {          var a = new Array("❤富强❤","❤民主❤","❤文明❤","❤和谐❤","❤自由❤","❤平等❤","❤公正❤","❤法治❤","❤爱国❤","❤敬业❤","❤诚信❤","❤友善❤");          var $i = $("<span></span>").text(a[a_idx]);          a_idx = (a_idx + 1) % a.length;          var x = e.pageX,          y = e.pageY;          $i.css({              "z-index": 999999999999999999999999999999999999999999999999999999999999999999999,              "top": y - 20,              "left": x,              "position": "absolute",              "font-weight": "bold",              "color": "rgb("+~~(255*Math.random())+","+~~(255*Math.random())+","+~~(255*Math.random())+")"          });          $("body").append($i);          $i.animate({              "top": y - 180,              "opacity": 0          },          1500,          function() {              $i.remove();          });      });  });  </script>

# [网页鼠标点击特效](https://www.cnblogs.com/wbyixx/p/11968619.html)