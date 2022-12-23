import { navbar } from "vuepress-theme-hope";

export const enNavbar = navbar([
  "/",
  { text: "Category", icon: "type", link: "/category/大数据🐘/" },
  { text: "Tags", icon: "tag", link: "/tag/python🐍/" },
  { text: "TimeLine", icon: "timer", link: "/timeline/" },
  {
    text: "About",
    icon: "others",
    prefix: "/articles",
    children: [
        { text: "Guide", icon: "launch", link: "/Guides/" },
        { text: "README", icon: "discover", link: "/README/" },

    ],
  },
]);
