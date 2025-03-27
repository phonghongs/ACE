import asyncio
from crawl4ai import AsyncWebCrawler

# List of URLs to crawl
urls = [
    "https://org.ngc.nvidia.com/setup/installers/cli",
    "https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#logging-in-to-ngc-registry",
    "https://docs.nvidia.com/ngc/index.html",
    "https://docs.docker.com/engine/install/",
    "https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html",
    "https://docs.docker.com/engine/install/linux-postinstall/",
    "https://github.com/NVIDIA/ACE",
    "https://docs.nvidia.com/ace/ace-agent/latest/deployment/docker-environment.html#docker-environment",
    "https://github.com/NVIDIA/ACE/tree/main/microservices/ace_agent/4.1",
    "https://docs.nvidia.com/ace/ace-agent/latest/reference/troubleshooting.html#troubleshooting",
    "https://docs.nvidia.com/ace/ace-agent/latest/deployment/sample-clients.html#sample-clients",
    "https://docs.nvidia.com/ace/ace-agent/latest/tutorials/build-bot-colang.html#build-bot-colang",
    "https://docs.nvidia.com/ace/ace-agent/latest/tutorials/build-langchain-bot.html#build-langchain-bot",
    "https://docs.nvidia.com/ace/ace-agent/latest/tutorials/build-bot-rag.html#build-bot-rag",
    "https://docs.nvidia.com/ace/ace-agent/latest/architecture/arch-intro.html#arch-intro",
    "https://www.nvidia.com/en-us/about-nvidia/privacy-policy/",
    "https://www.nvidia.com/en-us/about-nvidia/privacy-center/",
    "https://www.nvidia.com/en-us/preferences/start/",
    "https://www.nvidia.com/en-us/about-nvidia/terms-of-service/",
    "https://www.nvidia.com/en-us/about-nvidia/accessibility/",
    "https://www.nvidia.com/en-us/about-nvidia/company-policies/",
    "https://www.nvidia.com/en-us/product-security/",
    "https://www.nvidia.com/en-us/contact/"
]

async def crawl_and_save(url):
    crawler = AsyncWebCrawler(url)
    content = await crawler.crawl()
    file_name = url.replace("https://", "").replace("www.", "").replace("/", "_") + ".md"
    with open(file_name, "w", encoding="utf-8") as file:
        file.write(content)

async def main():
    tasks = [crawl_and_save(url) for url in urls]
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())
