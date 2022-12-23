<template>
  <div style="display:flex">
    <div class="pic"><img style="object-fit: cover" :src=cover></div>
    <div class="des" v-html="description"></div>
    <div class="verticalline"></div>
    <div class="rate">
      评分<span style="color: #f6ae32;font-family: 'Adobe Gothic Std';font-size: 35px">{{rate}}</span><br/>
      <div style="height: auto"></div>
      <div style="font-size: 10px">开始时间:<br/> {{startTime}}</div>
      <div style="font-size: 10px">结束时间:<br/> {{endTime}}</div>
      <span style="font-size: 20px">更多资料</span><br/>
      <div v-for="(item,address) in more">
        <span><a target="_blank" :href=item>{{ address }}</a></span> <br/>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: "CourseDisplayCard",
  props: ['id'],
  data() {
    return {
      cover: "http://static.ooowl.fun/s/aspcv9" ,//封面
      description: "none",//描述
      rate: "8.5",// 评分
      startTime: "2000-00-00 00:00:00",// 开始学习时间
      endTime: "2000-00-00 00:00:00",// 学完的时间
      more: { // 更多信息
        "豆瓣": "https://book.douban.com/",
        "b站": "https://www.bilibili.com"
      }
    }
  },
  mounted() {
    this.getData();
  },
  methods: {
    getData() {
      axios.get('/introduction/'+this.id+'.json').then(response => {
        this.$data.cover=response.data.cover // 图床地址额外配置在/.vuepress/public/js/pgmanor-self
        this.$data.description=response.data.description
        this.$data.rate=response.data.rate
        this.$data.startTime=response.data.startTime
        this.$data.endTime=response.data.endTime
        this.$data.more=response.data.more
        console.log(response.data);
      }, response => {
        console.log("error");
      });
    }
  }
}

</script>

<style scoped>
.pic{
  width: 170px;
  max-height: 300px;
  margin-right: 20px;
}
.des{
  width: 60%;
}
.rate{
  width: 15%;

}

.verticalline{
  margin-left: 20px;
  margin-right: 30px;
  width: 0;
  height: auto;
  opacity: 30%;
  border-left: 1px solid;
  border-color: #2c3e50;
}
</style>
