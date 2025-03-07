class MyUtils {
    work_of (pages, slice_at = null) {
        let tmp = pages.where((x) => x.word_count && (x.file.folder.indexOf("trash") < 0)).sort((x) => x.word_count, "desc").sort((x) => x.date ? x.date : x.auto_date, "desc")
        if (slice_at) {
            return tmp.slice(0, slice_at)
        }
        return tmp
    }

    meter_at (value, global) {
        const colors = [
            //hsl(0, 100%, 55%)
            { "h": 0, "s": 100, "l": 55, "v": 0 },
            //hsl(320, 100%, 60%)
            { "h": 320, "s": 100, "l": 60, "v": 0.25 },
            //hsl(240, 95%, 70%)
            { "h": 240, "s": 95, "l": 70, "v": 0.5 },
            //hsl(120, 60%, 45%)
            { "h": 120, "s": 60, "l": 45, "v": 0.75 },
            //hsl(60, 85%, 65%)
            { "h": 60, "s": 85, "l": 65, "v": 1 },
        ]
        let p = value
        let color = "hsl(0,100%,50%)"
        for (let i = 0; i < (colors.length - 1); i++) {
            if (colors[i].v <= p && p <= colors[i + 1].v) {
                let start_color = colors[i]
                let end_color = colors[i + 1]
                let position = (p - start_color.v) / (end_color.v - start_color.v)
                let h_inter = Math.abs(end_color.h - start_color.h) > 180 ? (end_color.h - start_color.h - 360) : (end_color.h - start_color.h)
                let h = start_color.h + position * h_inter
                h = h < 0 ? (h + 360) : (h > 360 ? (h - 360) : h)
                let s = start_color.s + position * (end_color.s - start_color.s)
                let l = start_color.l + position * (end_color.l - start_color.l)
                color = `hsl(${h},${s}%,${l}%)`
                break
            }
        }
        return `<meter value=${value} min=0 max=1 low=${global.percent_low} high=${global.percent_high} optimum=${global.percent_ideal} style="--progress-color: ${color};"></meter>`
    }

    percent_meter (value, global, separator = "") {
        return Math.round(value * 1000) / 10 + "%" + separator + this.meter_at(value, global)
    }

    count (page) {
        // return page.word_count
        let k = 0.32672845127999106
        let v = -69.5977971248443
        if (page.file.size < 500) {
            k = 0.2828777348112874
            v = -17.917200072765596
        } else if (page.file.size < 10000) {
            k = 0.3216869868584361
            v = -30.8130927729737
        } else if (page.file.size < 40000) {
            k = 0.3239843994825198
            v = -37.14210464748814
        }
        return Math.round(k * page.file.size + v)
    }

    count_sum (pages) {
        return pages.map(x => this.count(x)).sum()
    }

    count_text (value) {
        if (value < 20000) {
            return value + "字"
        }
        else {
            return Math.round(value / 100) / 100 + "万字"
        }
    }

    count_meter (page, global, line = 1) {
        let tmp = this.count(page)
        let percent = 1
        if (!page.finished) {
            percent = tmp / Math.max(tmp / global.percent_ideal, global.count_ideal)
        }
        if (line == 1) {
            return this.meter_at(percent, global) + " " + this.count_text(tmp)
        } else {
            return this.count_text(tmp) + "<br>" + this.meter_at(percent, global)
        }
    }

    last_update (page) {
        return Math.floor((Date.now() - Date.parse(page.date ? page.date : page.auto_date)) / 1000 / 60 / 60 / 24)
    }

    last_update_str (page) {
        let days = this.last_update(page)
        if (days == 0) {
            return "今天"
        } else if (days == 1) {
            return "昨天"
        } else if (days == 2) {
            return "前天"
        } else {
            return days + "天前"
        }
    }

    pin_of (page, global) {
        return "- [" + ((this.last_update(page) < Number(global.day_ideal)) ? "f" : "n") + "] "
    }

    short_text (page, global, tag_number = 2) {
        return this.pin_of(page, global) + page.file.link + " " + page.file.tags.slice(0, tag_number).join(" ") + " " + this.count_meter(page, global)
    }

    pages_raw_data (pages, global) {
        let all = this.work_of(pages)
        let tbc = all.where(page => !page.finished)
        let fin = all.where(page => page.finished)
        return {
            "tbc": tbc.length,
            "fin": fin.length,
            "all": all.length,
            "fin_percent": fin.length / all.length,
            "tbc_count": this.count_sum(tbc),
            "fin_count": this.count_sum(fin),
            "all_count": this.count_sum(all),
            "fin_count_avg": Math.round(fin.map(page => this.count(page)).avg()),
            "fin_count_theory": this.count_sum(fin) + tbc.map(x => Math.max(global.count_ideal, this.count(x) / global.percent_ideal)).sum()
        }
    }

    pages_data (pages, name, global) {
        // "名称","坑数","完结率","坑字数","完结字数比","平均完结字数"
        let raw_data = this.pages_raw_data(pages, global)
        return [
            name,
            raw_data.tbc,
            this.percent_meter(raw_data.fin_percent, global, 2),
            this.count_text(raw_data.tbc_count),
            this.percent_meter(raw_data.fin_count / raw_data.all_count, global, 2),
            this.count_text(raw_data.fin != 0 ? raw_data.fin_count_avg : 0)
        ]
    }
}