<template>
<div class="reHeader">
    <div class="headTop">
      <img class="topLogo" src="../assets/img/logo.png" />
      <div class="userbtn">{{getName}}，您好 <span  @click="waitlayout" class="layouticon">切换用户</span></div>
    </div>
    <ul class="headNav">
        <li v-for="item in datas" :key="item.cate_id" @click="emitGetNews(item.cate_id)" :class="active==item.cate_id ? 'navActive':''">{{item.cate_name}}</li>
        <li><a class="adminlink" :href="serverlink" target="_blank">进去后台</a></li>
    </ul>
</div>
</template>

<script>
import {mapGetters, mapActions} from 'vuex'
import {getCateData, layout} from '../assets/js/api'
import {serverUrl} from '../assets/js/linkBase'
export default {
  data () {
    return {
      datas: [],
      serverlink: ''
    }
  },
  props: {
    active: String
  },

  computed: {
    ...mapGetters('vuexlogin', {
      getLogin: 'getLogin',
      getName: 'getName'
    })
  },
  methods: {
    ...mapActions('vuexlogin', {
      almuta: 'almuta',
      almuuser: 'almuuser'
    }),
    emitGetNews: function (cateid) {
      this.$emit('onGetnews', {'cateid': cateid})
    },
    waitlayout: function () {
      this.$layer.confirm('确定退出当前用户，切换其他用户？', {title: '亲～'}, () => {
        this.layout()
        this.$layer.closeAll()
      })
    },
    layout: function () {
      layout().then((res) => {
        if (res.code) {
          localStorage.removeItem('newslogintime')
          localStorage.removeItem('username', '')
          localStorage.removeItem('islogin', false)
          this.almuta(localStorage.getItem('islogin'))
          this.almuuser(localStorage.getItem('username'))
          this.$router.push('/login')
        }
      }, (err) => {
        console.log(err)
      })
    },
    getCates: function () {
      this.loading('加载中。。。')
      getCateData().then((res) => {
        if (!res.code) {
          this.layout()
        } else {
          this.$layer.closeAll()
          this.datas = res.data
        }
      }, (err) => {
        this.$layer.msg('小主稍等，紧急恢复中。。。')
      })
    }
  },
  mounted () {
    this.serverlink = serverUrl + '/admin/'
    this.getCates()
  }
}
</script>

<style lang="less" scoped>
    @baseColor:red;
    #ellies(@n){
        overflow: hidden;
        text-overflow: ellipsis;
        display: -webkit-box;
        -webkit-line-clamp: @n;
        -webkit-box-orient: vertical;
    }
    .reHeader{
        .headTop{
          .userbtn{
            display: inline-block;
            float: right;
            line-height: 80px;
            margin-right: 5%;
            .layouticon{
              padding: 3px;
              border: 1px solid #eee;
              text-align: center;
              border-radius: 3px;
              background: #eee;
              margin-left: 10px;
              cursor: pointer;
              &:hover{
                background: #ddd;
              }
            }
          }
        }
        .headNav{
            display:flex;
            justify-content:flex-start;
            align-items: center;
            background: #ddd;
            height:40px;
        li{
            display: inline-block;
            width:120px;
            padding:5px 15px;
            box-sizing: border-box;
            position: relative;
            text-align: center;
            cursor: pointer;
            color: #555;
            .adminlink{
              text-decoration: none;
              color: #555;
              &:hover{
                color:#000
              }
            }
            &:hover{
              color:#000
            }
        }
        .navActive::after{
            content: " ";
            display: block;
            position: absolute;
            bottom: -6px;
            width: 30%;
            left: 50%;
            border-bottom: 2px solid @baseColor;
            margin-left: -15%;
            color:#000;
        }
        }
    }
</style>
