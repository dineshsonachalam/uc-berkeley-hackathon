import React from 'react';
import GenderStatsBarChart from './components/GenderStatsBarChart';
import RelationshipStatsBarChart from './components/RelationshipStatsBarChart';
import AdultStatsTable from './components/AdultStatsTable';
// import KingBattleRatingsLine from './components/KingBattleRatingsLine';
// import KingBattleWinLossPieChart from './components/KingBattleWinLossPieChart';
// import KingBattleDetailsTable from './components/KingBattleDetailsTable';
// import BattleStatsColumnChart from "./components/BattleStatsColumnChart";
// import BattleStatsTable from './components/BattleStatsTable';
// import KingDropDown from './components/KingDropDown';

import Nav from "./components/Nav"
import {  updateGenderStats, updateRelationshipStats, updateAdultStats } from "./redux/actions";
import { connect } from 'react-redux';

import { Layout} from 'antd';

const { Footer, Content } = Layout;

class App extends React.Component {
  async getData(url) {
    const response = await fetch(url);
    return response.json(); 
  }

  async componentDidMount(){
      let gender_stats_url = process.env.REACT_APP_API_ENDPOINT + "/gender/stats"
      let relationship_stats_url = process.env.REACT_APP_API_ENDPOINT + "/relationship/stats"
      let adult_stats_url = process.env.REACT_APP_API_ENDPOINT + "/adult/stats"
      const gender_stats_data = await this.getData(gender_stats_url);
      const relationship_stats_data = await this.getData(relationship_stats_url);
      const adult_stats_data = await this.getData(adult_stats_url);
      this.props.updateGenderStats(gender_stats_data);
      this.props.updateRelationshipStats(relationship_stats_data);
      this.props.updateAdultStats(adult_stats_data);
  }
  render(){
    return (
      <div className="App">
        <Nav />  
        <Content>
            <div style={{ padding: 24}}>
                    {this.props.gender_stats && (this.props.gender_stats).length>0 &&
                      <div>
                        <GenderStatsBarChart/>
                        <RelationshipStatsBarChart/>
                        <AdultStatsTable/>
                        {/* <KingBattleRatingsLine/>
                        <KingBattleWinLossPieChart/>
                        <KingBattleDetailsTable/>
                        <BattleStatsColumnChart/>
                        <BattleStatsTable/> */}
                      </div>
                    }
            </div>
        </Content>
        <div  style={ (this.props.gender_stats && (this.props.gender_stats).length>0) ? {}: { position:"absolute", bottom:0, color: "blue", width:"100%"  } }>
            <Footer style={{ textAlign: 'center' }}> Developed with ❤️ by <a href="https://github.com/dineshsonachalam/gender-diversity-metrics" rel="noreferrer" target="_blank">Dinesh Sonachalam</a> © {(new Date().getFullYear())}</Footer> 
        </div>
      </div>
    );
  }
}


const mapStateToProps = (state) => {
  return state.genderStatsReducer;
  
}

const mapDispatchToProps = (dispatch) => {
  return {
    updateGenderStats: (gender_stats) => dispatch(updateGenderStats(gender_stats)),
    updateRelationshipStats: (relationship_stats) => dispatch(updateRelationshipStats(relationship_stats)),
    updateAdultStats: (adult_stats) => dispatch(updateAdultStats(adult_stats))
  }
}

export default connect(mapStateToProps, mapDispatchToProps)(App);

