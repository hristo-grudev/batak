BOT_NAME = 'batak'

SPIDER_MODULES = ['batak.spiders']
NEWSPIDER_MODULE = 'batak.spiders'
FEED_EXPORT_ENCODING = 'utf-8'
LOG_LEVEL = 'ERROR'
DOWNLOAD_DELAY = 0

ROBOTSTXT_OBEY = True

ITEM_PIPELINES = {
	'batak.pipelines.BatakPipeline': 100,

}