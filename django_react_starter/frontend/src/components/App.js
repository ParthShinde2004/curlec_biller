import React from "react";
import { render } from "react-dom";
import Header from "./Header";
import BillingListForm from "./BillingListForm";
import InvoiceForm from "./InvoiceForm";
import ResultsTable from "./ResultsTable";

const App = () => {
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
          <BillingListForm />
        </div>
        <div
          className="grid-id-table"
          style={{
            padding: 10,
          }}
        >
          <ResultsTable />
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
};

const appDiv = document.getElementById("app");
render(<App />, appDiv);

/*
to do:
1. when you open console, settings button change
*/
