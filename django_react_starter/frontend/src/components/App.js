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

  setType(userinput) {
    this.setState({
      transactionType: userinput,
    });
  }

  setButton(status) {
    this.setState({
      buttonStatus: status,
    });
  }

  setCompany(company) {
    this.setState({
      selectedCompany: company,
    });
  }

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

/*
to do:
1. when you open console, settings button change
*/
