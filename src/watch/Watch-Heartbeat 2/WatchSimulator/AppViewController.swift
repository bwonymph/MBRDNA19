//
//  WatchAppViewController.swift
//  WatchSimulator
//

import UIKit

class AppViewController: UIViewController {

  @IBOutlet weak var bpmLabel: UILabel!
  var currentBeatPattern = BeatPattern()
  var currentBeatPatternIndex = 0

  var beatPatterns = [
    BeatPattern(icon: "💛", description: "Fast", bpm: 180),
    BeatPattern(icon: "❤️", description: "Mid-range", bpm: 80),
    BeatPattern(icon: "💜", description: "Slow", bpm: 55),
    BeatPattern(icon: "💙", description: "Sedated", bpm: 30),
  ]

  let iconLabel = UILabel()

  let shrinkFactor = CGFloat(2.0 / 3)
  var expandFactor: CGFloat {
    return 1.0 / shrinkFactor
  }

  override func viewDidLoad() {
    super.viewDidLoad()

    self.view.insertSubview(iconLabel, atIndex: 1)
  }
  
  override func viewWillAppear(animated: Bool) {
    super.viewWillAppear(animated)

    iconLabel.frame = self.view.bounds
    iconLabel.textAlignment = .Center
    iconLabel.font = UIFont.boldSystemFontOfSize(132)
  }
  
  override func viewDidAppear(animated: Bool) {
    super.viewDidAppear(animated)

    newBeat()

    NSTimer.scheduledTimerWithTimeInterval(8,
      target: self,
      selector: Selector("newBeat"),
      userInfo: nil,
      repeats: true)

    beat()
  }

  func newBeat() {
    //var bp = BeatPattern()
    // 1
    if ++currentBeatPatternIndex == beatPatterns.count {
      currentBeatPatternIndex = 0
    }

    // 2
    currentBeatPattern = beatPatterns[currentBeatPatternIndex]

    // 3
    bpmLabel.text = "\(currentBeatPattern.bpm)"
    iconLabel.text = currentBeatPattern.icon

    beatTrigger(currentBeatPattern.bpm)
  }

  func beat() {
    // 1
    UIView.animateWithDuration(currentBeatPattern.duration / 2,
      delay: 0.0,
      options: .CurveEaseInOut,
      animations: {
        // 2
        self.iconLabel.transform = CGAffineTransformScale(
          self.iconLabel.transform, self.shrinkFactor, self.shrinkFactor)
      },
      completion: { _ in
        // 3
        UIView.animateWithDuration(self.currentBeatPattern.duration / 2,
          delay: 0.0,
          options: .CurveEaseInOut,
          animations: {
            // 4
            self.iconLabel.transform = CGAffineTransformScale(
              self.iconLabel.transform, self.expandFactor, self.expandFactor)
          },
          completion: { _ in
            // 5
            self.beat()
          }
        )
      }
    )
  }

    func beatTrigger(heartRate: Int)
  {
    
    var alwaysTrue = true
    var myRootRef = Firebase(url:"https://benkpak.firebaseio.com/Watch/HeartRate")
    
    myRootRef.setValue(heartRate)
  }

}
