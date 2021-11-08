<template>
  <div id="app">
    <h1>My first Youtube Project</h1>
    <header>
      <the-search-bar @input-change="onInputChange"></the-search-bar>
    </header>

    <section>
      <div>
        <video-list :videos="vidoes"></video-list>
      </div>
    </section>
  </div>
</template>

<script>
import axios from 'axios'
import TheSearchBar from '@/components/TheSearchBar'

const API_KEY = 'AIzaSyADDzUFF_4BrOHosXk3WrJjDIYq2LJbyfQ'
const API_URL = 'https://www.googleapis.com/youtube/v3/search'

export default {
  name: 'App',
  components: {
    TheSearchBar
  },
  
  data: function () {
    return {
      inputValue: null,
      videos: [],
    }
  },
  methods: {
    onInputChange: function (inputValue) {
      this.inputValue = inputValue

      const params = {
        key: API_KEY,
        part: 'snippet',
        q: this.inputValue,
        type: 'video'
      }

      axios({
        method: 'get',
        url: API_URL,
        params,
      })
        .then(res => {
          console.log(res)
          this.videos = res.data.items
        })
        .catch(err => {
          console.log(err)
        })
    }
  },
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
