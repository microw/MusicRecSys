<template>
  <div class="newsContent">
    <new-header @onGetnews="returnMain" :active="CateId"></new-header>
    <div v-if="CateId == '2'" class="mainNews animated zoomIn" style="animation-duration:1s;animation-delay:0s">
      <div class="imgdesc">
        <img :src="datas.pl_img_url"/>
      </div>
      <div class="smalltitle">
        <h3 class="newsTitle">{{datas.pl_name}}</h3>
        <span class="newsAttribute">
          <i>作者：{{datas.pl_creator}}</i>
          <i>所属标签：{{datas.pl_tags}}</i>
        </span>
        <span class="newsAttribute">
          <i>评论次数：{{datas.pl_comment_num}}</i>
          <i>收藏人数：{{datas.pl_follow_num}}</i>
          <i>分享人数：{{datas.pl_share_num}}</i>
        </span>
        <span class="newsAttribute">
          <i>收录歌曲：{{datas.pl_songs_num}}</i>
          <i>收听次数：{{datas.pl_listen_num}}</i>
        </span>
        <span class="newsAttribute">
          <i>创建时间：{{datas.pl_create_time}}</i>
        </span>
        <span class="newsAttribute">
          <i>更新日期：{{datas.pl_update_time}}</i>
        </span>
      </div>
      <div class="news">介绍：{{datas.pl_desc}}</div>
      <audio id="audio"></audio>
      <ul class="songlist">
        <li class="songtitle" >
          <span>歌曲名称</span>
          <span>歌手名称</span>
          <span>播放状态</span>
        </li>
        <li v-for="item in datas.pl_songs" :key="item.song_id"  :class="playing == item.song_id ? 'song oksong' :'song'" @click="musicDesc({'id':item.song_id, 'cateid': '3'})">
          <span>{{item.song_name}}</span>
          <span v-if="item.song_sing_name">{{item.song_sing_name}}</span>
          <span v-else>未知歌手</span>
          <span v-if="playing != item.song_id" @click="playMusic({url:'../../static/music.m4a', id:item.song_id})">已暂停</span>
          <span @click="playMusic({url:'../../static/music.m4a', id:item.song_id})" v-else>播放中</span>
        </li>
      </ul>
    </div>
    <div v-if="CateId == '3'" class="mainNews animated zoomIn" style="animation-duration:1s;animation-delay:0s">
      <div class="imgdesc">
        <img src="../assets/img/music.png"/>
      </div>
      <div class="smalltitle">
        <h3 class="newsTitle">{{datas.song_name}}</h3>
        <span class="newsAttribute">
          <i>作者：{{datas.song_sing}}</i>
        </span>
        <span class="newsAttribute">
          <i>评论次数：{{datas.song_hot_comments}}</i>
          <i>热评次数：{{datas.song_total_comments}}</i>
        </span>
        <span class="newsAttribute">
          <i>创建时间：{{datas.song_publish_time}}</i>
        </span>
      </div>
      <h4 class="line">歌词</h4>
      <div class="news" v-html="datas.song_lysic"></div>
    </div>
    <div v-if="CateId == '4'" class="mainNews animated zoomIn" style="animation-duration:1s;animation-delay:0s">
      <div class="imgdesc singimg">
        <img :src="datas.sing_url"/>
      </div>
      <div class="smalltitle singsmalltitle">
        <h3 class="newsTitle">{{datas.sing_name}}</h3>
        <span class="newsAttribute">
          <i>专辑数：{{datas.sing_album_num}}</i>
          <i>歌曲数：{{datas.sing_music_num}}</i>
          <i>MV数：{{datas.sing_mv_num}}</i>
        </span>
      </div>
      <h4 class="line">系统录入单曲</h4>
      <ul class="songlist">
        <li class="songtitle" >
          <span>歌曲名称</span>
          <span>歌手名称</span>
          <span>播放状态</span>
        </li>
        <li v-for="item in datas.sing_songs" :key="item.song_id"  :class="playing == item.song_id ? 'song oksong' :'song'" @click="musicDesc({'id':item.song_id, 'cateid': '3'})">
          <span>{{item.song_name}}</span>
          <span>{{item.song_publish_time}}</span>
          <span v-if="playing != item.song_id" @click="playMusic({url:'../../static/music.m4a', id:item.song_id})">已暂停</span>
          <span @click="playMusic({url:'../../static/music.m4a', id:item.song_id})" v-else>播放中</span>
        </li>
      </ul>
    </div>
    <div v-if="CateId == '5'" class="mainNews animated zoomIn" style="animation-duration:1s;animation-delay:0s">
      <div class="imgdesc">
        <img :src="datas.u_img_url"/>
      </div>
      <div class="smalltitle">
        <h3 class="newsTitle">{{datas.u_name}}</h3>
        <span class="newsAttribute">
          <i>出生日期：{{datas.u_birthday}}</i>
          <i v-if="datas.u_gender === 0">性别：保密</i>
          <i v-else-if="datas.u_gender === 1">性别：男</i>
          <i v-if="datas.u_gender === 1">性别：女</i>
        </span>
        <span class="newsAttribute">
          <i>座右铭：{{datas.u_sign}}</i>
        </span>
        <span class="newsAttribute">
          <i>所属标签：{{datas.u_tags}}</i>
        </span>
      </div>
      <h4 class="line">创建的歌单</h4>
      <ul class="lists">
        <li class="titles" >
          <span>歌单图标</span>
          <span>歌单名称</span>
          <span>创建时间</span>
        </li>
        <li v-for="item in datas.u_playlist" :key="item.pl_id" @click="musicDesc({'id':item.pl_id, 'cateid': '2'})">
          <span>
            <img :src="item.pl_img_url" />
          </span>
          <span >{{item.pl_name}}</span>
          <span>{{item.pl_create_time}}</span>
        </li>
      </ul>
    </div>
    <div class="mainRight animated fadeInRight" style="animation-duration:1s;animation-delay:0.5s">
      <h3 class="hotTitle">相似推荐</h3>
      <ul class="relists">
        <li v-for="item in oneComment" :key="item.id" class="relist" @click="musicDesc({'id':item.id,'cateid':item.cate})">
          <img :src="item.img_url"/>
          <p class="recreater">{{item.creator}}</p>
          <p class="rename">{{item.name}}</p>
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
import {getplaylist, getsonglist, getsinglist, getuserlist} from '../assets/js/api'
import newHeader from '../components/newHeader.vue'
export default {
  name: 'news',
  data () {
    return {
      // 共同
      oneComment: {},
      CateId: '',
      // 列表
      datas: {},
      // music
      playing: ''
    }
  },
  components: {
    'new-header': newHeader
  },
  methods: {
    getNews: function (option) {
      this.loading('加载中。。。')
      option.username = this.$store.state.vuexlogin.userName
      if (this.CateId === '2') {
        getplaylist(option).then((res) => {
          this.$layer.closeAll()
          if (!res.code) {
            this.$children[0].layout()
          } else {
            res.data[0].pl_create_time = this.timeFormat(res.data[0].pl_create_time)
            res.data[0].pl_update_time = this.timeFormat(res.data[0].pl_update_time)
            this.oneComment = res.data[0].pl_rec
            this.datas = res.data[0]
          }
        }, (err) => {
          this.$layer.msg('小主稍等，紧急恢复中。。。')
        })
      } else if (this.CateId === '3') {
        getsonglist(option).then((res) => {
          this.$layer.closeAll()
          if (!res.code) {
            this.$children[0].layout()
          } else {
            res.data[0].song_publish_time = this.timeFormat(res.data[0].song_publish_time)
            this.oneComment = res.data[0].song_rec
            res.data[0].song_lysic = this.returnline(res.data[0].song_lysic, '\\\\n', '<br/>')
            this.datas = res.data[0]
          }
        }, (err) => {
          this.$layer.msg('小主稍等，紧急恢复中。。。')
        })
      } else if (this.CateId === '4') {
        getsinglist(option).then((res) => {
          this.$layer.closeAll()
          if (!res.code) {
            this.$children[0].layout()
          } else {
            this.oneComment = res.data[0].sing_rec
            res.data[0].sing_songs.forEach((item) => {
              item.song_publish_time = this.timeFormat(item.song_publish_time)
            })
            this.datas = res.data[0]
          }
        }, (err) => {
          this.$layer.msg('小主稍等，紧急恢复中。。。')
        })
      } else if (this.CateId === '5') {
        getuserlist(option).then((res) => {
          this.$layer.closeAll()
          if (!res.code) {
            this.$children[0].layout()
          } else {
            this.oneComment = res.data[0].u_rec
            res.data[0].u_playlist.forEach((item) => {
              item.pl_create_time = this.timeFormat(item.pl_create_time)
            })
            this.datas = res.data[0]
          }
        }, (err) => {
          this.$layer.msg('小主稍等，紧急恢复中。。。')
        })
      }
    },
    returnMain: function (option) {
      this.$router.push({name: 'home', params: option})
    },
    musicDesc: function (opt) {
      console.log(opt)
      this.$router.push({
        name: 'one',
        query: {cateid: opt.cateid, id: opt.id}
      })
      this.$router.go(0)
    },
    playMusic: function (opt) {
      var audio = document.getElementById("audio")
      audio.crossOrigin = 'anonymous'
      audio.src = opt.url
      if (this.playing === opt.id) {
        this.playing = ''
        audio.pause()
      } else {
        this.playing = opt.id
        audio.play()
      }
    }
  },
  mounted () {
    var Id = this.getUrlparams(window.location.href).id
    var cateid = this.getUrlparams(window.location.href).cateid
    this.CateId = cateid + ''
    this.getNews({'id': Id})
  }
}
</script>

<style lang="less" scoped>
  @baseColor:#20a0ff;
  #ellies(@n){
    overflow: hidden;
    text-overflow: ellipsis;
    -webkit-line-clamp: @n;
    -webkit-box-orient: vertical;
    white-space: nowrap;
  }
  .newsContent{
    width: 100%;
    box-sizing: border-box;
    padding: 2% 8%;
    overflow: auto;
    .mainNews{
      width: 70%;
      float: left;
      padding: 20px;
      box-sizing: border-box;
      padding-top: 0;
      margin-top:20px;
      .smalltitle{
        width: 50%;
        min-width: 340px;
        display: inline-block;
        vertical-align: top;
        .newsTitle{
          font-size: 20px;
          line-height: 36px;
          margin: 10px 0;
          font-weight: 600;
        }
        .newsAttribute{
          display: block;
          font-size: 12px;
          color:#999;
          height:18px;
          padding: 3px;
          i{
            display: inline-block;
            margin-left:25px;
            &:first-child{
              margin-left: 0;
            }
          }
        }
      }
      .imgdesc{
        display: inline-block;
        width: 150px;
        vertical-align: bottom;
        margin-right: 20px;
        img{
          width: 150px;
          height: 150px;
          border-radius: 80px;
        }
      }
      .singimg{
        display: block;
        margin:auto;
      }
      .singsmalltitle{
        display: block;
        width: 100%;
        text-align: center;
      }
      .news{
        color: #666;
        font-size: 14px;
        line-height: 25px;
        text-space: 2px;
        box-sizing: border-box;
        margin-top:10px;
      }
      .line{
        margin:10px 0;
        padding: 5px;
        box-sizing: border-box;
        background: #eee;
        color: #666;
      }
      .songlist{
        width: 100%;
        margin-top:15px;
        .song{
          height: 40px;
          line-height: 40px;
          color: #666;
          cursor: pointer;
          span{
            display: inline-block;
            #ellies(1);
            font-size: 12px;
          }
          span:first-child{
            width: 40%;
            min-width: 360px;
            font-size: 14px;
          }
          span:nth-child(2){
            width: 30%;
            min-width: 180px;
            font-size: 14px;
          }
          &:hover{
            color: @baseColor;
          }
        }
        .oksong{
          color: @baseColor;
        }
        .songtitle{
          height: 40px;
          line-height: 40px;
          color: #000;
          span{
            display: inline-block;
            #ellies(1);
            font-size: 12px;
          }
          span:first-child{
             width: 40%;
             min-width: 360px;
             font-size: 14px;
           }
          span:nth-child(2){
            width: 30%;
            min-width: 180px;
            font-size: 14px;
          }
        }
      }
      .lists{
        img{
          width: 120px;
          height: 120px;
          border-radius: 5px;
        }
        li{
          display: flex;
          justify-content: space-around;
          align-items: center;
          margin-top:20px;
          &:hover{
            color: @baseColor;
          }
        }
      }
    }
  .mainRight{
    width:30%;
    float:right;
    &>h3{
        width:100%;
        padding: 10px;
        margin-top:15px;
        background: #dfdfdfdf;
        vertical-align: middle;
        box-sizing: border-box;
      }
    .hotTitle{
      font-size: 18px;
      padding: 5px;
      color: #333;
      margin-bottom: 10px;
    }
    .relists{
      margin-top:20px;
      display: flex;
      justify-content: space-around;
      flex-wrap: wrap;
      .relist{
        width: 30%;
        box-sizing: border-box;
        padding: 5px;
        color: #333;
        cursor: pointer;
        margin-bottom: 15px;
        &:hover{
          color: @baseColor;
        }
        .recreater{
          font-size: 12px;
          color: #666;
          line-height: 14px;
          margin-bottom: 5px;
          margin-top: 5px;
          #ellies(1)
        }
        .rename{
          font-size: 14px;
          line-height: 16px;
          #ellies(1)
        }
        img{
          width: 100%;
        }
      }
      .singlists{
        width: 20%;
      }
      .onelist{
        width: 100%;
        color:#666;
        margin:5px 0;
        display: flex;
        justify-content: space-between;
        cursor: pointer;
        &:hover{
          color:@baseColor;
        }
        .onetime,.onename{
          #ellies(1);
          display: inline-block;
          box-sizing: border-box;
          padding: 0 10px;
        }
      }
    }
  }
  }

</style>
