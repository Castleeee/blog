import { defineClientConfig } from "@vuepress/client";

import Btn from "./components/Btn.vue";
import CourseDisplayCard from "./components/CourseDisplayCard.vue"
export default defineClientConfig({
    enhance: ({ app, router, siteData }) => {
        app.component("Btn", Btn);
        app.component("CourseDisplayCard", CourseDisplayCard);
    },
});
