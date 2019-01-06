<template>
    <div class="newFooter">
      <div class="footContent">
        <div class="footItem1">
          <h3>座右铭：</h3>
          <ul>
            <li>坚持，</li>
            <li>时间</li>
            <li>无论怎样的苦难喜甜，</li>
            <li>终将逝为云烟</li>
          </ul>
        </div>
        <div class="footItem2">
          <h3>微信公众号：</h3>
          <img class="bookcode" src="../assets/img/bookcode.jpg"/>
        </div>
        <div class="footItem3">
          <h3>我的小链：</h3>
          <ul>
            <li><a href="https://blog.csdn.net/gamer_gyt" target="_blank">CSDN</a></li>
            <li><a href="https://github.com/Thinkgamer" target="_blank">Github</a></li>
            <li><a href="https://weibo.com/234654758" target="_blank">我的微博</a></li>
          </ul>
        </div>
      </div>
      <div class="footCopy">
        <a href="https://github.com/Thinkgamer/NewsRecSys" target="_blank">©CopyRight thinkgamer</a>
        <span>本项目仅供演示，不做任何商业用途</span>
      </div>
    </div>
</template>

<script>
export default {
  name: 'newFooter'
}
</script>

<style lang="less" scoped>
  /*common style*/
  a{
    color:#777
  }
  a:hover{
    color:#333
  }
  .newFooter{
    display: flex;
    flex-flow: column;
    width: 100%;
    background: #f5f6f5;
    font-size: 12px;
    color: #777;
    .footContent{
      width: 100%;
      display: flex;
      justify-content: space-around;
      padding: 0 4%;
      box-sizing: border-box;
      .footItem1,.footItem2,.footItem3{
        width: 30%;
        padding:20px 5%;
        text-align: center;
        box-sizing: border-box;
        &>h3{
          margin-bottom:10px;
          display: inline-block;
          width: 100%;
        }
      }
      .footItem2>img{
        width: 50%;
      }
      .footItem1>ul li,.footItem3>ul li{
        margin-top:10px;
        margin-left: -10px;
      }
    }
    .footCopy{
      width: 100%;
      text-align: center;
      margin-top: 20px;
      margin-bottom: 15px;
    }
  }
</style>
