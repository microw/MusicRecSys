<template>
    <div class="login">
      <div v-if="!(showstep2 || showstep3)" class="loginstep">
        <div class=" posirelative select-out-div">
          <select class="userSelect" style="width: 120%; padding: 2px 0;" v-model="loginUser" name="userselect">
            <option value="">选择登陆用户</option>
            <option v-for="(item,index) in users" :key="index" :value="item">{{item}}</option>
          </select>
          <span class="select-hide-span" ><b class="select-show-b"></b></span>
        </div>
        <button class="nextBtn" @click="shownext(1)">下一步</button>
      </div>
      <div v-if="showstep2" class="loginstep2">
        <h3>选择喜爱的歌手</h3>
        <div class="alltag">
          <span class="tagbox" v-for="(tag,index) in sings" :key="index">
            <input type="checkbox" v-model="singsTags" name="singsbox" :value="index" />
            {{tag}}
          </span>
        </div>
        <div class="twobtn">
          <button class="skip" @click="shownext(3)">跳过</button>
          <button class="go" @click="shownext(2)">下一步</button>
        </div>
      </div>
        <div v-if="showstep3" class="loginstep2">
          <h3>选择喜爱的歌曲</h3>
          <div class="alltag">
          <span class="tagbox" v-for="(tag,index) in songs" :key="index">
            <input type="checkbox" v-model="songsTags" name="songsbox" :value="index" />
            {{tag}}
          </span>
          </div>
        <div class="twobtn">
          <button class="skip" @click="goLogin('skip')">跳过</button>
          <button class="go" @click="goLogin">进入系统</button>
        </div>
      </div>
    </div>
</template>

<script>
import {mapActions} from 'vuex'
import {getLogin, login} from '../assets/js/api'

export default {
  name: 'cyan',
  data () {
    return {
      users: {},
      tags: [],
      showstep2: false,
      loginUser: '',
      singsTags: [],
      songsTags: [],
      sings: {},
      songs: {},
      showstep3: false
    }
  },
  methods: {
    ...mapActions('vuexlogin', {
      almuta: 'almuta',
      almuuser: 'almuuser'
    }),
    shownext: function (n) {
      if (n === 1) {
        if (!this.loginUser) {
          this.$layer.alert('请输入要登陆的用户', {title: '温馨提示', btn: '好嘞，了解'})
          return false
        } else {
          this.showstep2 = true
        }
      } else if (n === 2) {
        if (this.singsTags.length < 3 && this.singsTags.length >= 0) {
          this.$layer.alert('至少选择三个标签哦', {title: '温馨提示', btn: '好哒'})
          return false
        } else {
          this.showstep2 = false
          this.showstep3 = true
        }
      } else if (n === 3) {
        this.showstep2 = false
        this.showstep3 = true
      }
    },
    goLogin: function (opt) {
      var logininfo = {
        username: this.loginUser,
        sings: '',
        songs: '',
        cate: 1,
        baseclick: 0
      }
      console.log(this.boxTags)
      if (opt && opt === 'skip') {
        logininfo.sings = ''
        logininfo.songs = ''
      } else {
        if (this.songsTags.length < 3 && this.songsTags.length >= 0) {
          this.$layer.alert('至少选择三个标签哦', {title: '温馨提示', btn: '好哒'})
          return false
        } else {
          logininfo.sings = this.singsTags.join(',')
          logininfo.songs = this.songsTags.join(',')
          this.singsTags = []
          this.songsTags = []
        }
      }
      console.log(logininfo)
      login(logininfo).then((res) => {
        if (res.code) {
          localStorage.setItem('newslogintime', new Date())
          this.almuta(true)
          this.almuuser(res.data.username)
          this.$router.push({path: '/', query: {'username': res.data.username, 'sings': res.data.sings, 'songs': res.data.songs, 'baseclick': 0}})
        }
      }, (err) => {
        console.log(err)
      })
    }
  },
  mounted () {
    getLogin().then((res) => {
      if (res.code === 1) {
        this.users = res.data.users
        this.sings = res.data.sings
        this.songs = res.data.songs
      }
    }, (err) => {
      console.log(err)
    })
  }
}
</script>

<style lang="less" scoped>
  #logins(){
    width: 40%;
    min-height: 300px;
    display: flex;
    flex-flow: column;
    justify-content: center;
    align-items: center;
    border: 1px solid #eee;
    padding-bottom: 20px;
    margin-bottom: 20px;
  }
  #btns(){
    background: #fff;
    height:35px;
    line-height: 35px;
    border:1px solid #999;
    border-radius: 5px;
    margin-top:10px;
    cursor: pointer;
    outline: none;
  }
  @baseColor:#20a0ff;
  .login{
    width: 100%;
    min-height: 500px;
    display: flex;
    justify-content: center;
    align-items: center;
    .loginstep{
      #logins();
      .posirelative {
        position: relative;
        width: 70%;
        overflow: hidden;
        margin-bottom: 30px;
        select.userSelect {
          background-color: #ffffff;
          background-image: none !important;
          filter: none !important;
          border: 1px solid #e5e5e5;
          outline: none;
          height: 35px !important;
          line-height: 35px;
        }
        .select-hide-span {
          height: 35px;
          position: absolute;
          top: 0;
          border-right: 1px solid #e5e5e5;
          right: 0;
          width: 20px!important;
          z-index: 999;
          .select-show-b {
            border-color: #888 transparent transparent transparent;
            border-style: solid;
            border-width: 5px 4px 0 4px;
            margin-left: -4px;
            margin-top: 15px;
            position: absolute;
          }
        }
      }
      .nextBtn{
        width: 60%;
        #btns();
        &:hover{
          color: #fff;
          background: @baseColor;
        }
      }
    }
    .loginstep2{
      #logins();
      justify-content: space-around;
      h3{
        margin-top:10px;
      }
      .twobtn{
        width: 100%;
        display: flex;
        justify-content:space-around;
        .skip,.go{
          width: 30%;
          #btns();
          &:hover{
            color: #fff;
            background: @baseColor;
          }
        }

        .skip:hover{
          background: #999;
        }
      }
      .alltag{
        padding: 10px;
        .tagbox{
          display: inline-flex;
          padding: 3px;
          border: 1px solid #999;
          border-radius: 3px;
          justify-content: center;
          align-items: center;
          margin:8px;
          input{
            cursor: pointer;
          }
        }
      }
    }
  }

</style>
