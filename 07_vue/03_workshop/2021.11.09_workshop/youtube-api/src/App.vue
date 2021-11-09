<template>
  <div id="app">
    <h1>My first Youtube Project</h1>
    <header>
      <search-Bar @input-change="onInputChange"></search-Bar>
    </header>
    <section>
      <video-detail :video="selectedVideo"></video-detail>
      <video-list :videos="videos" @select-video="onVideoSelect"></video-list>
    </section>

    <hello-world @click="onClick"></hello-world>
    <hello-world @click.native="onClick"></hello-world>
  </div>
</template>

<script>
import axios from 'axios'
import SearchBar from '@/components/SearchBar'
import VideoList from '@/components/VideoList'
import VideoDetail from '@/components/VideoDetail'
import HelloWorld from '@/components/HelloWorld.vue'


const API_KEY = process.env.VUE_APP_YOUTUBE_API_KEY
const API_URL = 'https://www.googleapis.com/youtube/v3/search'

export default {
  name: 'App',
  components: {
    SearchBar,
    VideoList,
    VideoDetail,
    HelloWorld,
  },
  data: function () {
    return {
      inputValue: null,
      videos: [],
      selectedVideo: null,
    }
  },
  methods: {
    onInputChange: function (inputValue) {
      // console.log(inputValue)
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
    },
    onVideoSelect: function (video) {
      this.selectedVideo = video
    },
    onClick: function() {
      console.log('Hello!')
    }
  }
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
