const API_URL = 'https://api.thecatapi.com/v1/images/search'
const app = new Vue({
  el: '#app',
  data: {
    imgSrc: '',
  },
  methods: {
    getImg: function() {
      axios.get(API_URL)
        .then(response => {
          console.log(response.data[0])
          this.imgSrc = response.data[0].url
        })
    },
    newCat() {
      axios.get(API_URL)
        .then(response => {
          this.imgSrc = response.data[0].url
        })
    },

  },
  created: function () {
    this.getImg()
  }
})