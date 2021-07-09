import React, { Component } from "react";

export class BillingListForm extends Component {
  state = {
    disabled: false,
    disabled2: false,
    buttonactivated: false,
  };

  handle_customerChange = (e) => {
    if (e.target.value !== "All") {
      this.setState({
        disabled: true,
      });
    } else {
      this.setState({
        disabled: false,
      });
    }
  };

  handle_paymentChange = (f) => {
    this.props.setButton("inactive");
    this.props.setType(f.target.value);
    if (f.target.value === "Mandate") {
      this.setState({
        disabled2: true,
      });
    } else {
      this.setState({
        disabled2: false,
      });
    }
  };

  buttonfunc = () => {
    this.props.setButton("active");
    this.props.setCompany(this.state.selectedchoice);
    this.props.setRefNo(this.state.selectedref);
  };

  constructor(props) {
    super(props);
    this.state = {
      data1: [],
      selectedchoice: -1,
      selectedref: -1,
    };
  }

  async componentDidMount() {
    const url = "http://127.0.0.1:8000/api/showmerchants";
    const response = await fetch(url);
    const data = await response.json();
    this.setState((prevState) => ({
      data1: data.data,
      selectedchoice: prevState.selectedchoice,
      selectedref: prevState.selectedref,
    }));
  }

  onTarget = (e) => {
    this.setState((prevState) => ({
      data1: prevState.data1,
      selectedchoice: e.target.value,
      selectedref: prevState.selectedref,
    }));
    console.log(e.target.value);
  };

  render() {
    return (
      <div className="card card-body mt-4 mb-4">
        <label>Customer</label>
        <form>
          <select
            className="form-control"
            aria-label=".form-select-sm example"
            onChange={this.onTarget}
          >
            <option value={-1}>Select Customer</option>
            <option value={"All"}>All</option>
            {this.state.data1.map((x, y) => (
              <option value={x.id} key={y}>
                {x.company_name}
              </option>
            ))}
          </select>
          <div className="form-group">
            <label style={{ margin: "8px 0px 0px" }}>From</label>
            <input className="form-control" type="date" />
          </div>

          <div className="form-group">
            <label>To</label>
            <input className="form-control" type="date" />
          </div>
          <label>Type</label>
          <select
            className="form-control"
            aria-label=".form-select-sm example"
            onChange={this.handle_paymentChange}
          >
            <option defaultValue>Select Type</option>
            <option value="Mandate">Mandate</option>
            <option value="Instant Pay (Bank)">Instant Pay (Bank)</option>
            <option value="Instant Pay (Card)">Instant Pay (Card)</option>
            <option value="Successful Pay (Bank)">Successful Pay (Bank)</option>
            <option value="Successful Pay (Card)">Successful Pay (Card)</option>
          </select>
          <div className="d-grid">
            <button
              type="button"
              className="btn btn-primary btn-block"
              style={{ margin: "10px 0px" }}
              onClick={this.buttonfunc}
            >
              Get Billing List
            </button>
          </div>

          <div className="btn-group d-md-flex mx-auto" role="toolbar">
            <button
              type="button"
              className="btn btn-outline-primary mr-2"
              style={{ minWidth: "205.5px" }}
              disabled={this.state.disabled || this.state.disabled2}
            >
              Export to Zip
            </button>
            <button
              type="button"
              className="btn btn-outline-primary"
              style={{ minWidth: "205.5px" }}
            >
              Export to Excel
            </button>
          </div>
        </form>
      </div>
    );
  }
}

export default BillingListForm;
