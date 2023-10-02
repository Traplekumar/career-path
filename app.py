import scrapeData
import metaphor
import gpt


def showResult(linkedin, career):
    try:
        driver = scrapeData.startDriver(linkedin)
        htmlSoup = scrapeData.getHTML(driver)
        name = scrapeData.getName(htmlSoup)
        headline = scrapeData.getHeadline(htmlSoup)
        about = scrapeData.getAbt(htmlSoup)
        experience = scrapeData.getExp(htmlSoup)
        education = scrapeData.getEdu(htmlSoup)
        certification = scrapeData.getCerti(htmlSoup)
        driver.quit()

        metaphorPrompt = metaphor.getPrompt(career)
        careerRaw = metaphor.search(metaphorPrompt)
        careerData = metaphor.getWebdata(careerRaw)

        gptResp = gpt.getResponse(about, experience, education, certification, careerData, career)    

        return gptResp
    except:
        return -1
