/* 2018-12-11
 *作者：qiaochaonan(cyan)
 *功能：
 */
const state = {
  isLogin: false,
  userName: ''
}
const actions = {
  almuta ({ commit, state }, loginState) {
    commit('alterLogin', loginState)
  },
  almuuser ({ commit, state }, newName) {
    commit('alterUser', newName)
  }
}
const getters = {
  getLogin (state) {
    if (!state.isLogin) {
      state.isLogin = localStorage.getItem('islogin')
    }
    return state.isLogin
  },
  getName (state) {
    if (!state.userName) {
      state.userName = localStorage.getItem('username')
    }
    return state.userName
  }
}

const mutations = {
  alterLogin (state, loginState) {
    if (loginState) {
      localStorage.setItem('islogin', true)
    } else {
      localStorage.removeItem('islogin')
    }
    state.isLogin = loginState
  },
  alterUser (state, newName) {
    if (newName) {
      localStorage.setItem('username', newName)
    } else {
      localStorage.removeItem('username')
    }
    state.userName = newName
  }
}

export default{
  namespaced: true,
  state,
  getters,
  actions,
  mutations
}
