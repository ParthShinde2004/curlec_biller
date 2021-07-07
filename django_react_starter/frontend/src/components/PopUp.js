import React, { Component } from "react";
import { Modal, Button } from "react-bootstrap";

export class PopUp extends Component {
  constructor(props) {
    super(props);
    this.state = {
      data1: [],
      selectedchoice: -1,
    };
  }

  async componentDidMount() {
    const url = "http://127.0.0.1:8000/api/showcalculations";
    const response = await fetch(url);
    const data = await response.json();
    this.setState((prevState) => ({
      data1: data.data,
      selectedchoice: prevState.selectedchoice,
    }));
  }

  onTarget = (e) => {
    this.setState((prevState) => ({
      data1: prevState.data1,
      selectedchoice: e.target.value,
    }));
  };

  render() {
    return (
      <Modal
        {...this.props}
        size="lg"
        aria-labelledby="contained-modal-title-vcenter"
        centered
      >
        <Modal.Header className="bg-primary">
          <Modal.Title id="contained-modal-title-vcenter" className="text-info">
            Calculation Rules Settings
          </Modal.Title>
          <button
            type="button"
            className="close"
            data-dismiss="modal"
            onClick={this.props.onHide}
          >
            <span aria-hidden="true" className="modal_button">
              &times;
            </span>
            <span className="sr-only">Close</span>
          </button>
        </Modal.Header>
        <Modal.Body>
          <h6>Customer</h6>
          <select
            className="form-control"
            aria-label=".form-select-sm example"
            onChange={this.onTarget}
          >
            <option value={-1}>Select Customer</option>
            {this.state.data1.map((x, y) => (
              <option value={y}>{x.company_name}</option>
            ))}
          </select>
          <h6>Calculation Rule - Credit Card:</h6>
          <div className="input-group">
            <a>
              {this.state.data1 &&
                this.state.selectedchoice != -1 &&
                this.state.data1[this.state.selectedchoice][
                  "calculation_rule_creditcard"
                ]}
            </a>
          </div>
          <h6>Calculation Rule - CASA:</h6>
          <div className="input-group">
            <a>
              {this.state.data1 &&
                this.state.selectedchoice != -1 &&
                this.state.data1[this.state.selectedchoice][
                  "calculation_rule_casa"
                ]}
            </a>
          </div>
          <h6>Calculation Rule - Instant Pay:</h6>
          <div className="input-group">
            <a>
              {this.state.data1 &&
                this.state.selectedchoice != -1 &&
                this.state.data1[this.state.selectedchoice][
                  "calculation_rule_instant_pay"
                ]}
            </a>
          </div>
          <h6>Calculation Rule - Monthly Dashboard Fee:</h6>
          <div className="input-group">
            <a>
              {this.state.data1 &&
                this.state.selectedchoice != -1 &&
                this.state.data1[this.state.selectedchoice][
                  "calculation_rule_creditcard"
                ]}
            </a>
          </div>
          <h6>Calculation Rule - Monthly Credit Card Fee:</h6>
          <div className="input-group">
            <a>
              {this.state.data1 &&
                this.state.selectedchoice != -1 &&
                this.state.data1[this.state.selectedchoice][
                  "calculation_rule_credit_card_fee"
                ]}
            </a>
          </div>
          <h6>Calculation Rule - Monthly Minimum Fee:</h6>
          <div className="input-group">
            <a>
              {this.state.data1 &&
                this.state.selectedchoice != -1 &&
                this.state.data1[this.state.selectedchoice][
                  "calculation_rule_minimum_fee"
                ]}
            </a>
          </div>
          {/* <h6>Calculation Rule - Monthly Mandate Fee:</h6>
          <div className="input-group">
            <textarea
              className="form-control"
              aria-label="With textarea"
            ></textarea>
          </div> */}
          <h6>Calculation Rule - Mandate Fee:</h6>
          <div className="input-group">
            <a>
              {this.state.data1 &&
                this.state.selectedchoice != -1 &&
                this.state.data1[this.state.selectedchoice][
                  "calculation_rule_mandate_fee"
                ]}
            </a>
          </div>
          <h6>Discount Rate - Credit Card:</h6>
          <div className="input-group">
            <a>
              {this.state.data1 &&
                this.state.selectedchoice != -1 &&
                this.state.data1[this.state.selectedchoice][
                  "calculation_rule_cc_discount"
                ]}
            </a>
          </div>
          <h6>Is Live</h6>
          <select className="form-control" aria-label=".form-select-sm example">
            <option defaultValue>Yes</option>
            <option value="1">No</option>
          </select>
        </Modal.Body>
        <Modal.Footer>
          <Button onClick={this.props.onHide}>Save</Button>
        </Modal.Footer>
      </Modal>
    );
  }
}

export default PopUp;
