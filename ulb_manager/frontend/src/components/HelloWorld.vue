<template>
  <div class="hello">
    <h2>接口测试</h2>
    <input type="button" value="接口测试" @click="testInterface">
    <ul>
      <li v-for="(item, index) in Data" :key="index + 'Data'">
        <ul>
          <li>bookName: {{item.fields.bookName}}</li>
          <li>fromSite: {{item.fields.fromSite}}</li>
          <li>fromUser: {{item.fields.fromUser}}</li>
          <li>updateTime: {{getDate(item.fields.updateTime)}}</li>
        </ul>
      </li>
    </ul>
  </div>
</template>

<script>
import Vue from 'vue'
export default {
  name: 'HelloWorld',
  data () {
    return {
      Data: []
    }
  },
  created () {},
  methods: {
    testInterface () {
      Vue.axios.get('api/bookInfo/get/').then((response) => {
        if (response.data) {
          this.Data = response.data
        }
      })
    },
    getDate (updateTime) {
      function formatDate (time) {
        const date = new Date(time)
        const year = date.getFullYear()
        const month = date.getMonth() + 1
        const day = date.getDate()
        const hour = date.getHours()
        const min = date.getMinutes()
        const sec = date.getSeconds()
        const newTime = year + '-' +
          (month < 10 ? '0' + month : month) + '-' +
          (day < 10 ? '0' + day : day) + ' ' +
          (hour < 10 ? '0' + hour : hour) + ':' +
          (min < 10 ? '0' + min : min) + ':' +
          (sec < 10 ? '0' + sec : sec)

        return newTime
      }

      return formatDate(new Date(updateTime).getTime())
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1, h2 {
  font-weight: normal;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
