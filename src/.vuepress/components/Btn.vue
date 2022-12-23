<template>
    <a id="homelink image-hero" href="/docs/guids">
      <button class="button1 button2">About me →</button>
    </a>
</template>

<script>
export default {
  name: "Btn"
}
</script>

<style scoped>
.button1 {
  margin:0 auto;
  box-shadow: 0 1px 2px 0 rgba(0,0,0,0.2), 0 3px 4px 0 rgba(0,0,0,0.19);
  border: 0px solid #4CAF50;
  border-radius: 5px;
  padding: 13px 20px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 20px;
  -webkit-transition-duration: 0.4s; /* Safari */
  transition-duration: 0.4s;
  cursor: pointer;
}
.button2 {
  background-color: #4cb9f2;
  text-decoration: none;
  color: #eef4fb;
  border: 0;
}
.button2:hover {
  background-color: rgba(0,111,255,0.88);
  text-decoration: none;
  color: white;
  box-shadow: 0 3px 5px 0 rgba(0,0,0,0.24), 0 10px 10px 0 rgba(0,0,0,0.19);
}
#homelink{
  position: absolute;
  padding-top: 200px;
  text-decoration: none;
}
</style>
