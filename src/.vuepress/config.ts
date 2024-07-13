import { defineUserConfig } from "vuepress";

import theme from "./theme.js";

export default defineUserConfig({
  base: "/",

  lang: "zh-CN",
  title: "萧箫的笔记仓库",
  // 整个文件的描述
  description: "",

  theme,

  // 和 PWA 一起启用
  // shouldPrefetch: false,
});
