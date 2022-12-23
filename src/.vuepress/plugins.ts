import {searchProPlugin} from "vuepress-plugin-search-pro";
import { live2dPlugin } from 'vuepress-plugin-live2d-plus'


export default function MyPlugin(){
    return [
    searchProPlugin({
        indexContent:true,
        customFields: [
            {
                name: "category",
                // @ts-ignore
                getter: (page) => page.frontmatter.category,
                formatter: {
                    "/": "分类：$content",
                },
            },
            {
                name: "tag",
                // @ts-ignore
                getter: (page) => page.frontmatter.tag,
                formatter: {
                    "/": "标签：$content",
                },
            },
        ],
    }),
    live2dPlugin({
        enable: true,
        model: {
            url: '/live2d-models/model-library/haru01/haru01.model.json'
        },
        display: {
            position: 'right',
            width: '135px',
            height: '300px',
            xOffset: '35px',
            yOffset: '-45px'
        },
        mobile: {
            show: true
        },
        react: {
            opacity: 0.8
        }
    }),

]}

