<template>
  <ul>
    <video-list-item
      v-for="(video, idx) in videos"
      :key="idx"
      :video="video"
    >

    </video-list-item>
  </ul>
</template>


<script>
import VideoListItem from '@/components/VideoListItem'


export default {
  name: 'VideoList',
  components: {
    VideoListItem,
  },
  props: {

  }
}
</script>

<style>

</style>
