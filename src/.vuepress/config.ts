import { defineUserConfig } from "vuepress";
import theme from "./theme.js";
import MyPlugin from "./plugins";

export default defineUserConfig({
  title:"会走路的三百块👾",
  base: "/",
  theme,
  plugins:MyPlugin(),
  shouldPrefetch: false,

});

