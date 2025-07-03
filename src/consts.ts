const SITE_TITLE = "狡兔百窟"
const SITE_DESCRIPTION = "兔子草的线上存档"
const SITE_AUTHOR = "兔子草"

const BUILTIN_THEME = [
  "light",
  "night",
  "cupcake",
  "bumblebee",
  "emerald",
  "corporate",
  "synthwave",
  "retro",
  "cyberpunk",
  "valentine",
  "halloween",
  "garden",
  "forest",
  "aqua",
  "lofi",
  "pastel",
  "fantasy",
  "wireframe",
  "black","luxury",
  "dracula",
  "cmyk",
  "autumn",
  "business",
  "acid",
  "lemonade",
  "night",
  "coffee",
  "winter",
  "dim",
  "nord",
  "sunset",
  "caramellatte",
  "abyss",
  "silk",
]

const LIGHT_THEME = "mylight"
const DARK_THEME = "mydark"
const EXTRA_TAGS = ["FIN", "TBC", "AI评论"]

import { unified } from "unified"
import remarkParse from "remark-parse"
import remarkGfm from "remark-gfm"
import remarkRehype from "remark-rehype"
import rehypeRaw from "rehype-raw"
import rehypeStringify from "rehype-stringify"

const processor = unified()
  .use(remarkParse)
  .use(remarkGfm)
  .use(remarkRehype, { allowDangerousHtml: true })
  .use(rehypeRaw)
  .use(rehypeStringify)

const cateNames: Record<string, string> = {
  ai: "评论",
  blob: "片段",
  dc: "DC",
  dm: "数码宝贝",
  dmc: "鬼泣",
  dr: "龙族",
  ft: "童话系列",
  gtm: "银魂",
  m: "漫威",
  on: "原创",
  others: "其他",
  qz: "全职",
  swy: "食物语",
  translation: "翻译",
  x: "X战警",
  xj: "仙剑",
  ywj: "曳尾记",
  yys: "阴阳师",
}

const cateName = (key: string) =>
  key in cateNames ? cateNames[key] : key.toUpperCase()

const date = (data: any) =>
  data.date ? data.date : data.auto_date || new Date("2018-01-01")

const SITE_ROOT = "/aoom"

const linkSite = (url: string) => SITE_ROOT + (url == "" ? "/" : url)

const linkStory = (id: string) => linkSite(`/docs/${id}`)

const linkName = (path: string) =>
  path == ""
    ? "首页"
    : path == "/docs"
      ? "所有文件"
      : cateName(decodeURIComponent(path.split("/").slice(-1)[0]))

const containsTag = (posts: Array<any>, tag: string) =>
  posts.filter((post) =>
    tag == "FIN"
      ? post.data.finished || post.data.ai_source
      : tag == "TBC"
        ? !post.data.finished
        : tag == "AI评论"
          ? post.data.ai_comment
          : post.data.tags.includes(tag)
  )
const matchCate = (posts: Array<any>, cate: string) =>
  posts.filter((post) => post.id.split("/")[0] == cate)

export {
  SITE_TITLE,
  SITE_AUTHOR,
  SITE_DESCRIPTION,
  SITE_ROOT,
  BUILTIN_THEME,
  LIGHT_THEME,
  DARK_THEME,
  EXTRA_TAGS,
  processor,
  cateName,
  date,
  linkName,
  linkSite,
  linkStory,
  containsTag,
  matchCate,
}
