
var lunchMenu = new Vue({
  el: '#lunchMenu',
  data: {
    modalLunch: false,
    menus: "",

  },

  methods: {
    myLunch() {
      this.modalLunch = true
      this.menus = _.sample(["곰탕", "오리탕", "감자탕", "사리곰탕"])

    },

    lunchModalClose() {
      this.modalLunch = false
    }

    },
})


var lottoNums = new Vue({
  el: '#lottoNums',
  data: {
    modalLotto: false,
    nums: "",
    bonus:"",
  },
  
  methods: {
    myLotto() {
      this.modalLotto = true
      this.bonus = _.sample(_.range(1,46))
      this.nums = _.sampleSize(_.range(1,46), 6)
      
    },

    lottoModalClose() {
      this.modalLotto = false
    }

  },
})