import React, { Component } from "react";
import { render } from "react-dom";
import Header from "./Header";
import BillingListForm from "./BillingListForm";
import InvoiceForm from "./InvoiceForm";
import ResultsTable from "./ResultsTable";

export default class App extends Component {
  state = {
    transactionType: "",
    buttonStatus: "",
    selectedCompany: "",
    selectedRefNo: "",
  };

  constructor(props) {
    super(props);
    this.setType = this.setType.bind(this);
    this.setButton = this.setButton.bind(this);
    this.setCompany = this.setCompany.bind(this);
    this.setRefNo = this.setRefNo.bind(this);
  }

  // used for 'ResultsTable.js' and sets the type (e.g. Mandate, Instant Pay, etc.)
  // to the variable name
  setType(userinput) {
    this.setState({
      transactionType: userinput,
    });
  }
  // used for 'ResultsTable.js' loading and sets the button status. Changes state when the
  // 'generate billing list' button is pressed
  setButton(status) {
    this.setState({
      buttonStatus: status,
    });
  }

  // used for 'ResultsTable.js' and assigns the variable with 'merchant_id'
  setCompany(company) {
    this.setState({
      selectedCompany: company,
    });
  }

  // failed attempt at passing 'ReferenceNumber'
  setRefNo(number) {
    this.setState({
      selectedRefNo: number,
    });
  }

  render() {
    return (
      <div>
        <Header />
        <div className="grid-container">
          <div
            className="grid-item grid-item-1"
            style={{
              width: 500,
              padding: 20,
            }}
          >
            {/* The billing list changes the states that are passed to results table. Add more when you create new APIs for succesful pay */}
            <BillingListForm
              setType={this.setType}
              setButton={this.setButton}
              setCompany={this.setCompany}
              setRefNo={this.setRefNo}
            />
          </div>
          <div
            className="grid-id-table"
            style={{
              padding: 10,
            }}
          >
            {/* The result table takes in all the states to generate all the tables. Add more when you create new APIs for succesful pay  */}
            <ResultsTable
              transactionType={this.state.transactionType}
              buttonStatus={this.state.buttonStatus}
              selectedCompany={this.state.selectedCompany}
              selectedRefNo={this.state.selectedRefNo}
            />
          </div>
          <div
            id="Invoice_Form"
            className="grid-item grid-item-3"
            style={{
              width: 500,
              padding: 20,
            }}
          >
            <InvoiceForm />
          </div>
        </div>
      </div>
    );
  }
}

const appDiv = document.getElementById("app");
render(<App />, appDiv);

// to do:
// 1. make sure the variable 'selectedRefNo' is passed correctly
