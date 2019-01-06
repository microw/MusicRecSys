<template>
  <div class="recommonContain">
    <mheader :active="isActive" @onGetnews="getCateMusic"> </mheader>
    <div v-if="isActive==1" class="mainContent">
      <div class="mainsign">
        <h3>歌单标签</h3>
        <ul class="lists">
          <li v-for="(item,index) in playlist.tags" :key="index" @click="getTagMusic(item+'+2')">{{item}}</li>
        </ul>
      </div>
      <div class="mainsign">
        <h3>歌曲标签</h3>
        <ul class="lists">
          <li v-for="(item,index) in song.tags" :key="index" @click="getTagMusic(item+'+3')">{{item}}</li>
        </ul>
      </div>
      <div class="mainsign">
        <h3>歌手标签</h3>
        <ul class="lists">
          <li v-for="(item,index) in sing.tags" :key="index" @click="getTagMusic(item+'+4')">{{item}}</li>
        </ul>
      </div>
    </div>
    <div v-if="isActive==2" class="mainContent">
      <div class="singCon singSongCon">
        <h3>歌单标签</h3>
        <ul class="signslists">
          <li :class="tag == 'all' ? 'oktag' : ''" @click="getTagMusic('all')">全部</li>
          <li :class="tag == item ? 'oktag' : ''" v-for="(item,index) in tags" :key="index" @click="getTagMusic(item)">{{item}}</li>
          <li v-if="tags.length <=15" class="moretag" @click="getmoreTag()">更多 >></li>
        </ul>
        <div class="allsign">
          <ul class="relists">
            <li v-for="item in plays" :key="item.pl_id" class="relist singlists" @click="musicDesc(item.pl_id)">
              <img :src="item.pl_img_url"/>
              <p class="recreater">{{item.pl_creator}}</p>
              <p class="rename">{{item.pl_name}}</p>
            </li>
          </ul>
        </div>
      </div>
      <div class="singCon singSong">
        <h3>歌单推荐</h3>
        <ul class="relists">
          <li v-for="item in replays" :key="item.pl_id" class="relist" @click="musicDesc(item.pl_id)">
            <img :src="item.pl_img_url"/>
            <p class="recreater">{{item.pl_creator}}</p>
            <p class="rename">{{item.pl_name}}</p>
          </li>
          <li class="more" @click="getCateMusic({'cateid': '6','rectag': '1'})">更多 >></li>
        </ul>
      </div>
    </div>
    <div v-if="isActive==3" class="mainContent">
      <div class="singCon singSongCon">
        <h3>歌曲标签</h3>
        <ul class="signslists">
          <li :class="tag == 'all' ? 'oktag' : ''" @click="getTagMusic('all')">全部</li>
          <li  :class="tag == item ? 'oktag' : ''" v-for="(item,index) in tags" :key="index" @click="getTagMusic(item)">{{item}}</li>
          <li v-if="tags.length <=15" class="moretag" @click="getmoreTag()">更多 >></li>
        </ul>
        <div class="allsign">
          <ul class="relists">
            <li v-for="item in songs" :key="item.song_id" class="onelist" @click="musicDesc(item.song_id)">
              <p class="onename">{{item.song_name}}</p>
              <p class="onetime">{{item.song_publish_time}}</p>
            </li>
          </ul>
        </div>
      </div>
      <div class="singCon singSong">
        <h3>歌曲推荐</h3>
        <ul class="relists">
          <li v-for="item in replays" :key="item.song_id" class="onelist" @click="musicDesc(item.song_id)">
            <p class="onename">{{item.song_name}}</p>
            <p class="onetime">{{item.song_publish_time}}</p>
          </li>
          <li class="more" @click="getCateMusic({'cateid': '6','rectag': '2'})">更多 >></li>
        </ul>
      </div>
    </div>
    <div v-if="isActive==4" class="mainContent">
      <div class="singCon singSongCon">
        <h3>歌手标签</h3>
        <ul class="signslists">
          <li :class="tag == 'all' ? 'oktag' : ''" @click="getTagMusic('all')">全部</li>
          <li :class="tag == item ? 'oktag' : ''" v-for="(item,index) in tags" :key="index" @click="getTagMusic(item)">{{item}}</li>
          <li v-if="tags.length <=15" class="moretag" @click="getmoreTag()">更多 >></li>
        </ul>
        <div class="allsign">
          <ul class="relists">
            <li v-for="item in sings" :key="item.sing_id" class="relist singlists" @click="musicDesc(item.sing_id)">
              <img :src="item.sing_url"/>
              <p class="recreater"></p>
              <p class="rename">{{item.sing_name}}</p>
            </li>
          </ul>
        </div>
      </div>
      <div class="singCon singSong">
        <h3>歌手推荐</h3>
        <ul class="relists">
          <li v-for="item in replays" :key="item.sing_id" class="relist" @click="musicDesc(item.sing_id)">
            <img :src="item.sing_url"/>
            <p class="recreater"></p>
            <p class="rename">{{item.sing_name}}</p>
          </li>
          <li class="more" @click="getCateMusic({'cateid': '6','rectag': '3'})">更多 >></li>
        </ul>
      </div>
    </div>
    <div v-if="isActive==5" class="mainContent">
      <div class="singCon singSongCon">
        <h3>用户标签</h3>
        <ul class="signslists">
          <li :class="tag == 'all' ? 'oktag' : ''" @click="getTagMusic('all')">全部</li>
          <li :class="tag == item ? 'oktag' : ''" v-for="(item,index) in tags" :key="index" @click="getTagMusic(item)">{{item}}</li>
          <li v-if="tags.length <=15" class="moretag" @click="getmoreTag()">更多 >></li>
        </ul>
        <div class="allsign">
          <ul class="relists">
            <li v-for="item in users" :key="item.u_id" class="relist singlists" @click="musicDesc(item.u_id)">
              <img :src="item.u_img_url"/>
              <p class="recreater"></p>
              <p class="rename">{{item.u_name}}</p>
            </li>
          </ul>
        </div>
      </div>
      <div class="singCon singSong">
        <h3>用户推荐</h3>
        <ul class="relists">
          <li v-for="item in replays" :key="item.u_id" class="relist" @click="musicDesc(item.u_id)">
            <img :src="item.u_img_url"/>
            <p class="recreater"></p>
            <p class="rename">{{item.u_name}}</p>
          </li>
        </ul>
      </div>
    </div>
    <div v-if="isActive==6" class="mainContent">
      <ul class="recnav">
        <li :class="rectag=='0'?'active':''" @click="getCateMusic({'cateid': '6', 'rectag': '0'})">总榜</li>
        <li :class="rectag=='1'?'active':''" @click="getCateMusic({'cateid': '6','rectag': '1'})">歌单</li>
        <li :class="rectag=='2'?'active':''" @click="getCateMusic({'cateid': '6','rectag': '2'})">歌曲</li>
        <li :class="rectag=='3'?'active':''" @click="getCateMusic({'cateid': '6','rectag': '3'})">歌手</li>
      </ul>
      <div class="mainsign" v-if="rectag=='0'">
        <h3>歌单榜<small style="font-size: 10px">(总榜显示前20)</small></h3>
        <ul class="lists musiclis">
          <li v-for="(item,index) in tmpplay" :key="index" @click="musicDesc(item.pl_id+'+2')">
            <b>
              <img :src="item.pl_img_url"/>
            </b>
            <span>{{item.pl_creator}}</span>
            <span>{{item.pl_name}}</span>
          </li>
        </ul>
      </div>
      <div class="mainsign" v-if="rectag=='0'">
        <h3>歌曲榜<small style="font-size: 10px">(总榜显示前20)</small></h3>
        <ul class="lists musiclis">
          <li v-for="(item,index) in tmpsong" :key="index" @click="musicDesc(item.song_id+'+3')">
            <span class="songname">{{item.song_name}}</span>
            <span class="songtime">{{item.song_publish_time}}</span>
          </li>
        </ul>
      </div>
      <div class="mainsign" v-if="rectag=='0'">
          <h3>歌手榜<small style="font-size: 10px">(总榜显示前20)</small></h3>
          <ul class="lists musiclis">
            <li v-for="(item,index) in tmpsing" :key="index" @click="musicDesc(item.sing_id+'+4')">
              <b>
                <img :src="item.sing_url"/>
              </b>
              <span class="singer">{{item.sing_name}}</span>
            </li>
          </ul>
        </div>
      <div class="mainsign singlemainsign" v-if="rectag=='1'">
        <ul class="lists musiclis">
          <li>
            <b class="icon">
              图标
            </b>
            <span>歌单名称</span>
            <span>歌单创建者</span>
            <span>歌单推荐值</span>
            <span>歌单创建时间</span>
          </li>
          <li v-for="(item,index) in sortplaylist" :key="index" @click="musicDesc(item.pl_id+'+2')">
            <b>
              <img :src="item.pl_img_url"/>
            </b>
            <span>{{item.pl_name}}</span>
            <span>{{item.pl_creator}}</span>
            <span>{{item.score}}</span>
            <span>{{item.pl_create_time}}</span>
          </li>
        </ul>
      </div>
      <div class="mainsign singlemainsign" v-if="rectag=='2'">
        <ul class="lists musiclis">
          <li>
            <span class="songname">歌曲名称</span>
            <span class="songname">歌曲演唱者</span>
            <span class="songname">歌曲推荐值</span>
            <span class="songname">歌曲创建时间</span>
          </li>
          <li v-for="(item,index) in sortsong" :key="index" @click="musicDesc(item.song_id+'+3')">
            <span class="songname">{{item.song_name}}</span>
            <span class="songtime">{{item.song_singer_name}}</span>
            <span class="songname">{{item.score}}</span>
            <span class="songtime">{{item.song_publish_time}}</span>
          </li>
        </ul>
      </div>
      <div class="mainsign singlemainsign" v-if="rectag=='3'">
        <ul class="lists musiclis">
          <li>
            <b class="icon">头像</b>
            <span class="singer">歌手名称</span>
            <span class="singer">专辑数</span>
            <span class="singer">歌曲数</span>
            <span class="singer">MV数</span>
            <span class="singer">歌手推荐值</span>
          </li>
          <li v-for="(item,index) in sortsing" :key="index" @click="musicDesc(item.sing_id+'+4')">
            <b>
              <img :src="item.sing_url"/>
            </b>
            <span class="singer">{{item.sing_name}}</span>
            <span class="singer">{{item.sing_album_num}}</span>
            <span class="singer">{{item.sing_music_num}}</span>
            <span class="singer">{{item.sing_mv_num}}</span>
            <span class="singer">{{item.score}}</span>
          </li>
        </ul>
      </div>
    </div>
    <div v-if="isActive==7" class="mainContent">
      <ul class="liscan">
        <li>
          <span>时间</span>
          <span>操作</span>
        </li>
        <li v-for="(item,index) in datas" :key="index">
          <span>{{item.time}}</span>
          <span>{{item.desc}}<b v-if="item.name">【{{item.name}}】</b> </span>
        </li>
      </ul>
    </div>
    <div class="rightpag">
      <mpagnation v-if="total>display" :total="total" :current-page='current' :refresh='refresh' @pagechange="pagechange"></mpagnation>
    </div>
   </div>
</template>

<script>
import {getCateMusicData, getRecommon} from '../assets/js/api'
import newheader from '../components/newHeader.vue'
import pagnation from '../components/pagnation'
export default {
  name: 'HelloWorld',
  data () {
    return {
      isActive: '1',
      newsData: {},
      tmptags: [],
      // playlist
      playlist: {},
      song: {},
      sing: {},
      // 歌单相关
      tags: [],
      plays: {},
      replays: [],
      // 歌曲相关
      songs: [],
      // 歌手相关
      sings: [],
      // 用户相关
      users: [],
      // 分页相关
      total: 0, // 总条数
      current: 1, // 当前激活页
      display: 30, // 每页显示多少条
      refresh: false, // 是否刷新（第一页激活）有搜索时需要
      tag: 'all',
      // 足迹
      datas: [],
      // 排行榜
      sortplaylist: [],
      sortsong: [],
      sortsing: [],
      tmpplay: [],
      tmpsing: [],
      tmpsong: [],
      // 排行榜分榜标示
      rectag: '0'
    }
  },
  components: {
    'mheader': newheader,
    'mpagnation': pagnation
  },
  methods: {
    getCateMusic: function (option) {
      let cateId = option.cateid
      let getdata = {}
      if (!option.tag) {
        option.tag = 'all'
      }
      if (!option.page) {
        option.page = 1
      }
      if (!option.rectag) {
        this.rectag = '0'
      } else {
        this.rectag = option.rectag
      }
      this.tag = option.tag
      if (cateId === '1') {
        this.loading('加载中。。。')
        if (option.sings) {
          getdata.sings = option.sings
          getdata.songs = option.songs
          getdata.baseclick = option.baseclick
        } else {
          getdata.sings = ''
          getdata.songs = ''
          getdata.baseclick = option.baseclick
        }
        if (option.baseclick === '0') {
          getdata.baseclick = 0
        } else {
          getdata.baseclick = 1
        }
        getdata.cateid = '1'
        this.isActive = cateId + ''
        getdata.username = this.$store.state.vuexlogin.userName
        getCateMusicData(getdata).then((res) => {
          this.$layer.closeAll()
          if (!res.code) {
            this.$children[0].layout()
          } else {
            this.playlist = res.data.playlist
            this.sing = res.data.sing
            this.song = res.data.song
          }
        }, (err) => {
          this.$layer.msg('小主稍等，紧急恢复中。。。')
        })
      } else {
        this.loading('加载中。。。')
        if (cateId) {
          getdata.cateid = cateId
          getdata.sings = ''
          getdata.songs = ''
          getdata.baseclick = 1
          getdata.tag = option.tag
          getdata.page = option.page
          this.isActive = cateId + ''
        }
        getdata.username = this.$store.state.vuexlogin.userName
        var recommonData = {
          'cateid': cateId,
          'username': getdata.username
        }
        if (recommonData.cateid === '2' || recommonData.cateid === '3' || recommonData.cateid === '4' || recommonData.cateid === '5') {
          getRecommon(recommonData).then((res) => {
            if (res.code === 1) {
              if (recommonData.cateid === '2') {
                this.replays = res.data.recplaylist
              } else if (recommonData.cateid === '3') {
                res.data.songs.forEach((item) => {
                  item.song_publish_time = this.timeFormat(item.song_publish_time)
                })
                this.replays = res.data.songs
              } else if (recommonData.cateid === '4') {
                this.replays = res.data.sings
              } else if (recommonData.cateid === '5') {
                this.replays = res.data.users
              }
            }
          })
        }
        var allrec = (cateId === '6' && this.rectag === '0' && this.sortplaylist.length > 0 && this.sortsing.length > 0 && this.sortsong.length > 0)
        var playrec = (cateId === '6' && this.rectag === '1' && this.sortplaylist.length > 0)
        var songrec = (cateId === '6' && this.rectag === '2' && this.sortsong.length > 0)
        var singrec = (cateId === '6' && this.rectag === '3' && this.sortsing.length > 0)
        if (!(allrec || playrec || singrec || songrec)) {
          getCateMusicData(getdata).then((res) => {
            this.$layer.closeAll()
            if (!res.code) {
              this.$children[0].layout()
            } else {
              if (res.data.tags) {
                this.tags = res.data.tags.slice(0, 15)
                this.tmptags = res.data.tags
              }
              if (getdata.cateid === '2') {
                this.plays = res.data.playlist
                this.total = res.data.total
              } else if (getdata.cateid === '3') {
                res.data.songs.forEach((item) => {
                  item.song_publish_time = this.timeFormat(item.song_publish_time)
                })
                this.songs = res.data.songs
                this.total = res.data.total
              } else if (getdata.cateid === '4') {
                this.sings = res.data.sings
                this.total = res.data.total
              } else if (getdata.cateid === '5') {
                this.users = res.data.sings
                this.total = res.data.total
              } else if (getdata.cateid === '6') {
                this.total = 1
                res.data.song.forEach((item) => {
                  item.song_publish_time = this.timeFormat(item.song_publish_time)
                })
                res.data.playlist.forEach((item) => {
                  item.pl_create_time = this.timeFormat(item.pl_create_time)
                })
                this.tmpplay = res.data.playlist.slice(0, 20)
                this.tmpsing = res.data.sing.slice(0, 20)
                this.tmpsong = res.data.song.slice(0, 20)
                if (this.rectag === '1') {
                  this.sortplaylist = res.data.playlist
                } else if (this.rectag === '2') {
                  this.sortsong = res.data.song
                } else if (this.rectag === '3') {
                  this.sortsing = res.data.sing
                } else {
                  this.sortplaylist = res.data.playlist
                  this.sortsing = res.data.sing
                  this.sortsong = res.data.song
                }
              } else if (getdata.cateid === '7') {
                res.data.click.forEach((item) => {
                  item.time = this.timeFormat(item.time)
                })
                this.total = res.data.total
                this.datas = res.data.click
              }
            }
          }, (err) => {
            this.$layer.msg('小主稍等，紧急恢复中。。。')
          })
        } else {
          this.$layer.closeAll()
          return 0
        }
      }
    },
    musicDesc: function (id) {
      if (id.indexOf('+') > -1) {
        var tmpid = id.split('+')
        id = tmpid[0]
        this.isActive = tmpid[1]
        console.log(tmpid[1])
      }
      this.$router.push({
        name: 'one',
        query: {id: id, cateid: this.isActive}
      })
    },
    // 分页
    pagechange: function (currentPage) {
      this.tags = this.tags.slice(0, 15)
      this.refresh = false
      this.page = currentPage
      // 滚到顶部 注意不在window而在document.documentElement
      document.documentElement.scrollTop = 0
      document.body.scrollTop = 0
      // 获取列表 可根据后端要求改变page的方式
      this.getCateMusic({'page': this.page, 'cateid': this.isActive, 'tag': this.tag})
    },
    // tag获取
    getTagMusic: function (nowtag) {
      this.tags = this.tags.slice(0, 15)
      this.refresh = true
      this.tag = nowtag
      if (nowtag.indexOf('+') > -1) {
        var tmptag = nowtag.split('+')
        this.tag = tmptag[0]
        this.isActive = tmptag[1]
      }
      this.getCateMusic({'cateid': this.isActive, 'tag': this.tag})
    },
    // 获取更多tag
    getmoreTag: function () {
      this.tags = this.tmptags
    }
  },
  mounted () {
    // this.getCateMusic({'cateid': '2'})
    var sings = this.$route.query.sings
    var songs = this.$route.query.songs
    var baseclick = this.$route.query.baseclick + ''
    if (this.$route.params.cateid) {
      this.getCateMusic({'cateid': this.$route.params.cateid})
    } else {
      this.getCateMusic({'cateid': '1', 'sings': sings, 'songs': songs, 'baseclick': baseclick})
    }
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
  .recommonContain{
    width: 100%;
    padding:2% 8%;
    padding-bottom: 0;
    box-sizing: border-box;
    .mainContent{
      width: 100%;
      display: flex;
      box-sizing: border-box;
      justify-content: space-around;
      .mainsign{
        width: 32%;
        box-sizing: border-box;
        padding:10px;
        border:1px solid #ddd;
        margin:15px 30px;
        box-shadow: 0 0 5px 5px #eee;
        min-height: 300px;
        .lists {
          margin-top: 10px;
          li {
            padding: 6px 8px;
            border-radius: 4px;
            color: #333;
            font-size: 16px;
            width: auto;
            display: inline-block;
            border: 1px solid #ddd;
            cursor: pointer;
            margin: 5px;
          }
          li:first-child{
            color: orange;
            border: 1px solid orange;
          }
          li:nth-child(2){
            color: red;
            border: 1px solid red;
          }
          li:nth-child(3){
            color: coral;
            border: 1px solid coral;
          }
          li:nth-child(4){
            color: chocolate;
            border: 1px solid chocolate;
          }
          li:hover {
            color: @baseColor;
            border: 1px solid @baseColor;
          }
        }
        .musiclis{
          li{
            width: 100%;
            box-sizing: border-box;
            b{
              img{
                width: 50px;
                height:50px;
                border-radius: 25px;
              }
            }
            span{
              display: inline-block;
              width: 30%;
              #ellies(1);
              vertical-align: middle;
              font-size: 12px;
            }
            span:last-child{
              font-size: 14px;
              width: 43%;
              float: right;
              line-height: 50px;
            }
            span.songname{
              font-size: 14px;
              width: 50%;
            }
            span.songtime{
              font-size: 12px;
              width: 37%;
            }
            span.singer{
              width: 65%;
            }
          }
        }
      }
      .singlemainsign{
        width: 100%;
        .lists{
          li{
            display: flex;
            justify-content: space-around;
            align-items: center;
            .icon{
              width: 140px;
            }
            span{
              margin-left: 15px;
            }
          }
          li:first-child{
            color: #666;
            border: none;
          }
          li:first-child:hover {
            color: #666;
            border: none;
          }
        }
      }
      .singCon{
        box-sizing: border-box;
        padding:10px;
        border:1px solid #ddd;
        box-shadow: 0 0 5px 5px #eee;
        min-height: 500px;
        margin-top:15px;
        margin-bottom: 15px;
        .signslists{
          margin-top:10px;
          li{
            display: inline-block;
            border: 1px solid #ddd;
            box-sizing: border-box;
            padding: 6px;
            border-radius: 4px;
            margin:5px;
            text-align: center;
            cursor: pointer;
            font-size: 12px;
            &:hover{
              color: @baseColor;
              border: 1px solid @baseColor;
            }
          }
          .oktag{
            color: @baseColor;
            border: 1px solid @baseColor;
          }
          .moretag{
            color: orange;
            border: 1px solid orange;
          }
        }
        .relists{
          margin-top:20px;
          display: flex;
          justify-content: space-around;
          flex-wrap: wrap;
          .more{
            padding: 5px;
            border:1px solid orange;
            color:#fff;
            background: orange;
            text-align: center;
            width: 120px;
            border-radius: 3px;
            height: 30px;
            line-height: 30px;
            margin-top:15px;
            cursor: pointer;
          }
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
      .singSongCon{
        flex: 2;
        margin-right: 15px;
      }
      .singSong{
        flex: 1;
        margin-left: 15px;
        min-width: 30%;
      }
      .liscan{
        width: 100%;
        li{
          width: 100%;
          color: #666;
          font-size: 14px;
          display: block;
          margin:20px;
          span{
            display: inline-block;
            width: 40%;
          }
        }
        li:first-child{
          color: #000;
        }
      }
      .recnav{
        width: 10%;
        min-width: 120px;
        padding-left: 20px;
        margin-top:20px;
        box-sizing: border-box;
        li{
          width: 100%;
          height: 30px;
          box-sizing: border-box;
          line-height: 30px;
          padding-left: 20px;
          color: #666;
          cursor: pointer;
        }
        .active{
          background: #eee;
          box-shadow: 10px 0px 10px 1px @baseColor;
        }
      }
    }
    .rightpag{
      width: 70%;
    }
  }
</style>
