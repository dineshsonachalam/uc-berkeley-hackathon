import React from "react";
import { Table} from "antd";
import { connect } from "react-redux";
import { PageHeader} from "antd";
class AdultStatsTable extends React.Component { 
      render() {
            const columns = [
                  {
                        title: "Age",
                        dataIndex: "age",
                        key: "id",
                  },
                  {
                        title: "Education",
                        dataIndex: "education",
                        key: "education"
                  },
                  {
                        title: "Marital status",
                        dataIndex: "marital_status",
                        key: "marital_status",
                  },
                  {
                        title: "Native country",
                        dataIndex: "native_country",
                        key: "native_country",
                  },
                  {
                        title: "Salary",
                        dataIndex: "salary",
                        key: "salary",
                  },
                  {
                        title: "Gender",
                        dataIndex: "sex",
                        key: "sex",
                        width: "20%",
                  }
            ]; 
            return (
                <div>
                        {(this.props.adult_stats).length>0 &&     
                              <div className="site-page-header-ghost-wrapper">
                              <PageHeader
                                title="Employees detail by gender in Chicago, USA"
                              >
                                    <Table columns={columns} dataSource={this.props.adult_stats} onChange={this.handleTableChange} />
                              </PageHeader>
                              </div> 
                        }
                </div>
            );
      }
}



const mapStateToProps = (state) => {
      return state.genderStatsReducer;
}
    
const mapDispatchToProps = (dispatch) => {
      return {}
}
    
export default connect(mapStateToProps, mapDispatchToProps)(AdultStatsTable);