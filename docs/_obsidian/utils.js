class MyUtils {
    work_of (pages, slice_at = null) {
        let tmp = pages.where((x) => x.word_count && (x.file.folder.indexOf("trash") < 0)).sort((x) => x.word_count, "desc").sort((x) => x.date ? x.date : x.auto_date, "desc")
        if (slice_at) {
            return tmp.slice(0, slice_at)
        }
        return tmp
    }

    meter_at (value, global) {
        return `<meter value=${value} min=0 max=1 low=${global.percent_low} high=${global.percent_high} optimum=${global.percent_ideal}></meter>`
    }

    percent_meter (value, global, separator = "") {
        return Math.round(value * 1000) / 10 + "%" + separator + this.meter_at(value, global)
    }

    count (page) {
        // return page.word_count
        let k = 0.32672891800857884
        let v = -69.75555350528298
        if (page.file.size < 500) {
            k = 0.28292381653162024
            v = -17.97134616568257
        } else if (page.file.size < 10000) {
            k = 0.32165039119903244
            v = -30.868579490654348
        } else if (page.file.size < 40000) {
            k = 0.3239850419968106
            v = -37.300838880213256
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