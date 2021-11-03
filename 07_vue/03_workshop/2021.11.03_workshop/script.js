
var lunchMenu = new Vue({
  el: '#lunchMenu',
  data: {
    menus: "",

  },

  methods: {
    myLunch() {
      return this.menus = _.sample(["곰탕", "오리탕", "감자탕", "사리곰탕"])

    },

    },
})


var lottoNums = new Vue({
  el: '#lottoNums',
  data: {
    nums: "",
    bonus:"",
  },
  methods: {
    myLotto() {
      this.bonus = _.sample(_.range(1,46))
      this.nums = _.sampleSize(_.range(1,46), 6)
      
    } 
  },
})