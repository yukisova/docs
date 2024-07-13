import { navbar } from "vuepress-theme-hope";

// 导航栏接收数组，数组的每一个元素都代表着一个链接
export default navbar([
  // 字符串格式链接
  // 直接作为超链接项使用，更加进一步的信息要在，对应文件中设置
  // 可以省略.md后缀名，完全省略文件名的话默认访问其中的README文件
  
  // "/",
  // "/portfolio",
  // "/demo/",

  // // 对象格式链接
  // // 相对于字符串能够进行完整的页面Meta设置
  // {
  //   // 项目名称
  //   text: "指南",

  //   // 项目图标
  //   icon: "lightbulb",

  //   // 项目激活匹配
  //   activeMatch: "",

  //   // 用于对下拉列表链接进行简化，要加在children前
  //   prefix: "/guide/",
  //   link:""
  // },
  // {
  //   text: "V2 文档",
  //   icon: "book",
  //   link: "https://theme-hope.vuejs.press/zh/",
  // },
]);
