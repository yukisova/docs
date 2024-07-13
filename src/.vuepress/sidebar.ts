import { sidebar } from "vuepress-theme-hope";

// 相比较于导航栏，侧边栏必须要使用对象
export default sidebar({
  // 根目录，以类似梳妆结构的方式
  "/": [
    // 这里实际上与导航栏配置方式相似
    "",
    {
      text: "Python学习",
      prefix: "dirPython/",
      children: "structure"
    },
    {
      text: "小工具",
      prefix: "dirUseful/",
      children: "structure"
    },
    {
      text: "前端",
      prefix: "dirFrontend/",
      children: "structure"
    },
    {
      text: "Java学习",
      prefix: "dirJava/",
      children: "structure"
    },
    {
      text: "C++学习",
      prefix: "dirCpp/",
      children: "structure"
    },
    {
      text: "Linux学习",
      prefix: "dirShell/",
      children: "structure"
    },
    {
      text: "自创小说",
      prefix: "dirNovel/",
      children: "structure"
    },
    {
      text: "某段时刻的灵光一现",
      prefix: "dirAnynote/",
      children: "structure"
    },
    // {
    //   text: "案例",
    //   icon: "laptop-code",
    //   prefix: "demo/",
    //   link: "demo/",
    //   children: "structure",

    //   // 设置分组是否可折叠
    //   // collapsible:false;

    //   // 设置分组是否默认展开
    //   // expanded: false;
    // },
  ],
});
