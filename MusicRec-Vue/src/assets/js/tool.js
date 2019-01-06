/** 2018/12/11
 *作者:qiaochaonan(cyan)
 *功能:全局功能函数
 */
exports.install = function (Vue, options) {
  // 时间格式化
  Vue.prototype.timeFormat = function (time) {
    if (!time) return false
    var datetime = new Date(time)
    var y = datetime.getFullYear()
    var m = datetime.getMonth() + 1 < 10 ? '0' + parseInt(datetime.getMonth() + 1) : parseInt(datetime.getMonth() + 1)
    var d = datetime.getDate() < 10 ? '0' + datetime.getDate() : datetime.getDate()
    var h = datetime.getHours() < 10 ? '0' + datetime.getHours() : datetime.getHours()
    var mm = datetime.getMinutes() < 10 ? '0' + datetime.getMinutes() : datetime.getMinutes()
    var s = datetime.getSeconds() < 10 ? '0' + datetime.getSeconds() : datetime.getSeconds()
    return y + '年' + m + '月' + d + '日   ' + h + ':' + mm + ':' + s
  }
  // 获取URL
  Vue.prototype.getUrlparams = function (url) {
    let urlArr = url.split('?')
    if (urlArr < 2) return false
    let tmpArr = urlArr[1].split('&')
    var result = {}
    tmpArr.forEach(item => {
      let tmppar = item.split('=')
      result[tmppar[0]] = tmppar[1]
    })
    return result
  }
  // 处理文本换行不匹配
  Vue.prototype.returnline = function (str, reg, replacestr) {
    let re = new RegExp(reg, 'g')
    str = str.replace(re, replacestr)
    return str
  }
  // 数据加载缓冲
  Vue.prototype.loading = function (msg) {
    this.$layer.msg(msg, {
      time: 3600,
      shade: true,
      shadeClose: false
    })
  }
  // 时间差计算
  Vue.prototype.deTime = function (time, newtime, efftime) {
    let t1 = new Date(time)
    let t2 = new Date(newtime)
    let detime = parseInt(t2 - t1) / 1000 / 3600
    // console.log(detime + 'iiii' + efftime)
    if (detime > efftime) {
      this.$children[0].$children[0].layout()
    }
  }
}
