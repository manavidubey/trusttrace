library(shiny)
pacman::p_load(rio)
bank<-import("bank.xlsx")
ui<-fluidPage(
    navbarPage(
      "Transaction Analysis",
      tabPanel(
        "Graphical Overview",
        
        sidebarPanel(
          tags$h3("Account Number"),
          tags$h4("Please press ' just after entering the Account Number."),
          textInput("txt1","","")
          
        ),
        
        mainPanel(
          tags$h3("Withdrawl Overview :-"),
          plotOutput(outputId<-"wa"),
          tags$h3("Deposit Overview"),
          plotOutput(outputId<-"da"),
          tags$h3("Maximum Transactions :-"),
          tableOutput(outputId<-"ss"),
          tags$h3("Maximum Withdrawl Transaction details:-"),
          tableOutput("waa"),
          tags$h3("Maximum Deposit Transaction details:-"),
          tableOutput(outputId<-"daa")
          
          
        )
      ),
      
      tabPanel(
        "Withdrawl History",
        sidebarPanel(
          tags$h3("Account Number"),
          tags$h4("Please press ' just after entering the Account Number."),
          textInput("txt2","","")
          
        
      ),
      
      mainPanel(
        tags$h3("Withdrawl details :-"),
        tableOutput(outputId<-"with")
        
      )
      
    ),
    
    tabPanel(
      "Deposit History",
      sidebarPanel(
        tags$h3("Account Number"),
        tags$h4("Please press ' just after entering the Account Number."),
        textInput("txt3","","")
        
    ),
    
    mainPanel(
      tags$h3("Deposit Details :-"),
      tableOutput(outputId<-"depo")
    )
    )
    )
)
   
 

server<-function(input,output){
  output$wa<-renderPlot({
    waa<-bank$`WITHDRAWAL AMT`[bank$`Account No`==input$txt1]
    plot(waa)
  })
  output$da<-renderPlot({
    daa<-bank$`DEPOSIT AMT`[bank$`Account No`==input$txt1]
    plot(daa)
  })
    
  output$with<-renderTable({
    withdrawl<-bank$`WITHDRAWAL AMT`[bank$`Account No`==input$txt2]
    transaction_details<-bank$`TRANSACTION DETAILS`[bank$`Account No`==input$txt2]
    na.omit(data.frame(transaction_details,withdrawl))
  })
  
  output$depo<-renderTable({
    deposit<-bank$`DEPOSIT AMT`[bank$`Account No`==input$txt3]
    transaction_details<-bank$`TRANSACTION DETAILS`[bank$`Account No`==input$txt3]
    na.omit(data.frame(transaction_details,deposit))
  })
  
  output$ss<-renderTable({
    withdrawl<-bank$`WITHDRAWAL AMT`[bank$`Account No`==input$txt1]
    deposit<-bank$`DEPOSIT AMT`[bank$`Account No`==input$txt1]
    maximum_withdrawl<-max(na.omit(withdrawl))
    maximum_deposit<-max(na.omit(deposit))
    data.frame(maximum_withdrawl,maximum_deposit)
  })
  
  output$waa<-renderTable({
    withdrawl<-bank$`WITHDRAWAL AMT`[bank$`Account No`==input$txt1]
    maximum_withdrawl<-max(na.omit(withdrawl))
    table(bank$`TRANSACTION DETAILS`[bank$`Account No`==input$txt1 & bank$`WITHDRAWAL AMT`==maximum_withdrawl])
    
    
    
  })
  
  output$daa<-renderTable({
    deposit<-bank$`DEPOSIT AMT`[bank$`Account No`==input$txt1]
    maximum_deposit<-max(na.omit(deposit))
    table(bank$`TRANSACTION DETAILS`[bank$`Account No`==input$txt1 & bank$`DEPOSIT AMT`==maximum_deposit])
    
    
  })
  
  
  
  
}

shinyApp(ui = ui,server = server)