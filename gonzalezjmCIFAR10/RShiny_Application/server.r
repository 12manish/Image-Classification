
library(shiny)
cvData <- read.csv(file = "/home/spring2016_csci334user13/img_app/cvData.csv")

shinyServer(function(input, output) {

  output$plot1 <- renderPlot({
    name = input$class
    
    if (name=="RFC") {
      boxplot(cvData$rfc)
    } else if (name=="LDA") {
      boxplot(cvData$lda)
    } else {
      boxplot(cvData$knn)
    }
    
  })
  
  output$plot2 <- renderPlot({
    name = input$class
    
    if (name=="RFC") {
      y <- cvData[,1]
      name = "PCA -> Random Forest Classification"
    } else if (name=="LDA") {
      y <- cvData[,2]
      name = "PCA -> Linear Discriminant Analysis"
    } else {
      y <- cvData[,3]
      name = "PCA -> K-Nearest Neighbor"
    }
    x <- 1:10
    
    
  
    plot(x,y,main=paste("10-Fold Cross Validation for", name),xlab="Cross-Validation Iteration",
         ylab="Accuracy",ylim=c(0,1),col = 'black')
  })
  
  output$plot3 <- renderPlot({
    boxplot(cvData, main="Accuracy by Classification")  
  })
  
  output$getStats <- renderText({
    
    name = input$class
    
    if (name=="RFC") { 
      rfcPlot <- boxplot(cvData$rfc)
      paste(rfcPlot$stats)

    } else if (name=="LDA") {
      ldaPlot <- boxplot(cvData$lda)
      paste(ldaPlot$stats)
    } else {
      knnPlot <- boxplot(cvData$knn)
      paste(knnPlot$stats)
    }
    
  })
  
})

