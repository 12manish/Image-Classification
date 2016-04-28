
library(shiny)
shinyUI(fluidPage(
  
  titlePanel("Image Classification"),
  
  sidebarLayout(
    sidebarPanel(
      selectInput('class', 'Classifier', list("PCA -> Random Forest Classification" = "RFC", 
                                              "PCA -> Linear Discriminant Analysis" = "LDA", 
                                              "PCA -> K-Nearest Neighbor" = "KNN"))
    ),
    
    mainPanel(
      tabsetPanel(
        tabPanel("Box Plot",
                 plotOutput("plot1"),
                 h4("Five Number Summary: MIN, Q1, Q2, Q3, MAX"),
                 textOutput("getStats")
        ),
        tabPanel("Dot Plot",
                 plotOutput("plot2")
        ),
        tabPanel("Box Plot Comparison",
                 plotOutput("plot3")
        )     
      )
      
    )
  )
))

