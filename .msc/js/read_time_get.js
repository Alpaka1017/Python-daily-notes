<script>
  // 获取文本内容
  var content = document.body.textContent;

  // 计算字数和字符数
  var wordCount = content.trim().split(/\s+/).length;
  var charCount = content.length;

  // 计算预计阅读时间（假设平均阅读速度为每分钟200个单词）
  var readingTime = Math.ceil(wordCount / 200);

  // 将结果显示在页面中
  document.write('字数：' + wordCount + '<br>');
  document.write('字符数：' + charCount + '<br>');
  document.write('预计阅读时间：' + readingTime + '分钟');
</script>
